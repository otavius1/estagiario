import requests
import os

numero_processo = input("Digite o número do processo (apenas números, sem pontos ou traços): ")

response = requests.get(f"http://127.0.0.1:8000/consulta?numero_processo={numero_processo}")

print(response.status_code)
print(response.text)

if response.status_code == 200:
    data = response.json()
    if "relatorio_html" in data:
        
        os.makedirs("data", exist_ok=True)
        caminho_arquivo = f"data/{numero_processo}.html"
        
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(data["relatorio_html"])
        
        print(f"Relatório salvo em: {caminho_arquivo}")
    else:
        print("A API retornou sucesso, mas não há relatorio_html.")
else:
    print("Erro ao consultar o processo ou API não respondeu corretamente.")

