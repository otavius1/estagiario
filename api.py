from fastapi import FastAPI, Query
from bot.services import consultar_processo_api_service
from auth.routes import router as users_router

app = FastAPI()

@app.get("/consulta")
async def consulta(numero_processo: str = Query(...)):
    return await consultar_processo_api_service(numero_processo)

app.include_router(users_router)