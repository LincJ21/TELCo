from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from db.user_register_db import crear_usuario

router = APIRouter()

@router.post("/registro", response_class=HTMLResponse)
async def registro(request: Request):
    form_data = await request.form()
    nombre = form_data.get("nombre")
    edad = form_data.get("edad")
    email = form_data.get("email")
    password = form_data.get("password")
    
    if not nombre or not edad or not email or not password:
        raise HTTPException(status_code=400, detail="Por favor, complete todos los campos.")
    
    # Aquí puedes llamar a la función para crear el usuario en la base de datos
    # Suponiendo que `crear_usuario` es una función definida en tu archivo de base de datos
    usuario_creado = crear_usuario(nombre, edad, email, password)
    
    if usuario_creado:
        return HTMLResponse(content="<h1>Usuario creado correctamente</h1>")
    else:
        raise HTTPException(status_code=500, detail="Error al crear el usuario.")
