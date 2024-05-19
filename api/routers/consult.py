from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
#from templates import consult
from db import consult_db

router = APIRouter()

@router.get("/consulta", response_class=HTMLResponse)
async def consulta(request: Request):
    # Obtener datos de la base de datos
    data = consult_db()
    if data:
        return "Error al obtener datos de la base de datos"
        #return consult.render(data=data)  # Renderizar el template con los datos
    else:
        return "Error al obtener datos de la base de datos"
