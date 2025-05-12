import subprocess
import sys
import json
import os
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

USE_SUBPROCESS = os.getenv("USE_SUBPROCESS", "True").lower() == "true"

if not USE_SUBPROCESS:
    from bot.utils import formatar_numero_processo
    from bot.navegador import abrir_site, consultar_processo
    from bot.scraper import extrair_andamentos, extrair_dados_processo
    from bot.relatorio import gerar_html

async def consultar_processo_api_service(numero_processo: str):
    if not numero_processo or not numero_processo.isdigit():
        raise HTTPException(status_code=400, detail="Número do processo inválido. Envie apenas números.")

    if USE_SUBPROCESS:
        try:
            result = subprocess.run(
                [sys.executable, "main.py", numero_processo],
                capture_output=True,
                text=True,
                timeout=120 
            )
        except subprocess.TimeoutExpired:
            raise HTTPException(status_code=504, detail="Timeout ao executar subprocesso do bot.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro inesperado no subprocesso: {str(e)}")

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Erro no subprocesso: {result.stderr}")

        try:
            return json.loads(result.stdout)
        except Exception:
            raise HTTPException(status_code=500, detail="Falha ao decodificar JSON do subprocesso.")
        
    else:
        numero_formatado = formatar_numero_processo(numero_processo)
        try:
            playwright, browser, page = await abrir_site()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao iniciar browser: {str(e)}")

        try:
            nova_aba = await consultar_processo(page, numero_formatado)
            html_content = await nova_aba.content()

            dados = extrair_dados_processo(html_content)
            dados['numero'] = numero_formatado
            andamentos = extrair_andamentos(html_content)
            relatorio_html = gerar_html(dados, andamentos)

            return {"numero": numero_formatado, "relatorio_html": relatorio_html}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao consultar processo: {str(e)}")
        finally:
            await browser.close()
            await playwright.stop()
