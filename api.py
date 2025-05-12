from fastapi import FastAPI, Query
from bot.services import consultar_processo_api_service

app = FastAPI()

@app.get("/consulta")
async def consulta(numero_processo: str = Query(...)):
    return await consultar_processo_api_service(numero_processo)