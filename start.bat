@echo off
echo =======================================
echo Iniciando Estagiário Jurídico (modo Windows)
echo =======================================
echo.

echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando dependências...
pip install -r requirements.txt

echo Iniciando servidor FastAPI...
uvicorn api:app --reload

pause
