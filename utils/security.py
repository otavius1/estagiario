from passlib.context import CryptContext

# Cria o contexto de hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica se a senha em texto puro corresponde ao hash armazenado.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Gera o hash seguro de uma senha.
    """
    return pwd_context.hash(password)
