import requests
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = os.getenv("API_PORT", "8000")
DATA_DIR = os.getenv("DATA_DIR", "data")

# Garantir que a pasta existe
os.makedirs(DATA_DIR, exist_ok=True)

numero_processo = input("Digite o número do processo (apenas números, sem pontos ou traços): ")

response = requests.get(f"http://{API_HOST}:{API_PORT}/consulta?numero_processo={numero_processo}")

print(response.status_code)
print(response.text)

if response.status_code == 200 and "relatorio_html" in response.json():
    nome_arquivo = f"{numero_processo}.html"
    caminho_arquivo = os.path.join(DATA_DIR, nome_arquivo)

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(response.json()["relatorio_html"])

    print(f"Relatório salvo em {caminho_arquivo}")
else:
    print("Erro ao consultar o processo ou relatório não gerado.")
