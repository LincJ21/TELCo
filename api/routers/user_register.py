from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from db.user_register_db import crear_usuario

# Crear una instancia del enrutador de FastAPI
router = APIRouter()

@router.post("/registro", response_class=HTMLResponse)
async def registro(request: Request):
    """
    Endpoint para registrar un nuevo usuario.
    
    Args:
        request (Request): La solicitud HTTP, que debe contener datos del formulario con los campos:
            - nombre (str): Nombre del usuario.
            - edad (str): Edad del usuario.
            - email (str): Email del usuario.
            - password (str): Contraseña del usuario.

    Returns:
        HTMLResponse: Respuesta HTML indicando si el usuario fue creado correctamente.

    Raises:
        HTTPException: Si falta algún campo del formulario (status code 400) o si ocurre un error al crear el usuario (status code 500).
    """
    # Obtener datos del formulario
    form_data = await request.form()
    nombre = form_data.get("nombre")
    edad = form_data.get("edad")
    email = form_data.get("email")
    password = form_data.get("password")
    
    # Verificar que todos los campos estén completos
    if not nombre or not edad or not email or not password:
        raise HTTPException(status_code=400, detail="Por favor, complete todos los campos.")
    
    # Llamar a la función para crear el usuario en la base de datos
    usuario_creado = crear_usuario(nombre, edad, email, password)
    
    # Verificar si el usuario fue creado correctamente
    if usuario_creado:
        return HTMLResponse(content="<h1>Usuario creado correctamente</h1>")
    else:
        raise HTTPException(status_code=500, detail="Error al crear el usuario.")
