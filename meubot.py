import sys
import asyncio
import json
from bot.utils import formatar_numero_processo
from bot.scraper import extrair_andamentos, extrair_dados_processo
from bot.relatorio import gerar_html
from bot.navegador import abrir_site, consultar_processo

async def main():
    if len(sys.argv) != 2:
        print(json.dumps({"status": "erro", "detalhe": "Uso: python meubot.py <numero_processo>"}))
        return

    numero = sys.argv[1]
    numero_formatado = formatar_numero_processo(numero)

    playwright, browser, page = await abrir_site()
    try:
        nova_aba = await consultar_processo(page, numero_formatado)
        html_content = await nova_aba.content()

        dados = extrair_dados_processo(html_content)
        dados['numero'] = numero_formatado
        andamentos = extrair_andamentos(html_content)
        relatorio_html = gerar_html(dados, andamentos)

        print(json.dumps({
            "numero": numero_formatado,
            "relatorio_html": relatorio_html
        }))
    except Exception as e:
        print(json.dumps({"status": "erro", "detalhe": str(e)}))
    finally:
        await browser.close()
        await playwright.stop()

if __name__ == "__main__":
    asyncio.run(main())
