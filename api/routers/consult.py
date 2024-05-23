from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from db import consult_db  # Importar la función para consultar la base de datos

# Crear una instancia del enrutador de FastAPI
router = APIRouter()

@router.get("/consulta", response_class=HTMLResponse)
async def consulta(request: Request):
    """
    Endpoint para consultar datos de la base de datos y renderizarlos como HTML.

    Args:
        request (Request): La solicitud HTTP entrante.

    Returns:
        HTMLResponse: La respuesta HTML con los datos consultados o un mensaje de error.
    """
    # Obtener datos de la base de datos
    data = consult_db()
    
    if data:
        # Renderizar el template con los datos obtenidos de la base de datos
        # return consult.render(data=data)  # Descomentar esta línea cuando el template esté disponible
        return HTMLResponse(content=f"<html><body><h1>Datos: {data}</h1></body></html>")  # Placeholder para renderización
    else:
        return HTMLResponse(content="Error al obtener datos de la base de datos")
