# cli.py
import requests
import os

def main():
    numero_processo = input("Digite o número do processo (apenas números, sem pontos ou traços): ").strip()
    url = f"http://127.0.0.1:8000/consulta?numero_processo={numero_processo}"
    
    print(f"Consultando API para o processo {numero_processo}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "relatorio_html" in data:
            os.makedirs("data", exist_ok=True)
            caminho = os.path.join("data", f"{data['numero']}.html")
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(data["relatorio_html"])
            print(f"Relatório salvo com sucesso em: {caminho}")
        else:
            print("A API respondeu mas não retornou relatorio_html.")
    else:
        print(f"Erro ao consultar a API. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()
