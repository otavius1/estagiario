import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Importar base, model e settings
from database.base import Base
from core.settings import settings  # 👈 Seu settings está agora em core
from database.models.user import User 

# Alembic config
config = context.config
fileConfig(config.config_file_name)

# 👇 FUNÇÃO mágica que troca async por sync só para Alembic
def get_sync_url():
    return settings.database_url.replace("+aiomysql", "+pymysql")

# Setar URL sync para Alembic
config.set_main_option("sqlalchemy.url", get_sync_url())

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
