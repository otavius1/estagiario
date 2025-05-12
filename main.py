# main.py

from bot.navegador import abrir_site, consultar_processo
from bot.scraper import extrair_andamentos
from bot.utils import formatar_numero_processo
from bot.relatorio import gerar_html

def main():
    numero_puro = input("Digite o número do processo (apenas números, sem traços/pontos): ")
    numero_formatado = formatar_numero_processo(numero_puro)
    print(f"Consultando processo: {numero_formatado}")

    page = abrir_site()
    nova_aba = consultar_processo(page, numero_formatado)

    andamentos = extrair_andamentos(nova_aba)

    print("\nAndamentos encontrados:")
    for andamento in andamentos:
        print(f"{andamento['data']} - {andamento['evento']}")

    # 💡 MOCK: dados_processo provisórios para gerar HTML
    dados_processo = {
        'numero': numero_formatado,
        'classe': 'Ação Penal - Procedimento Ordinário',
        'assunto': 'Crimes Previstos no Estatuto do Idoso',
        'vara': '5ª Vara Criminal de Brasília',
        'partes': [
            'MINISTÉRIO PÚBLICO DO DF E DOS TERRITÓRIOS',
            'FRANCIANA APARECIDA ALMEIDA XAVIER (Réu)',
            'Advogados: Ricardo Souza, Tayana Barros'
        ]
    }

    html = gerar_html(dados_processo, andamentos)
    print("\nHTML GERADO PARA ENVIO:")
    print(html)

if __name__ == "__main__":
    main()

    
# 0716108-14.2021.8.07.0016