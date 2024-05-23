from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from sso.google_sso import GoogleSSO, SSOLoginError

# Crear una instancia del enrutador de FastAPI
router = APIRouter()

# Datos proporcionados para la autenticación con Google
GOOGLE_CLIENT_ID = "GOOGLE_CLIENT_ID"
GOOGLE_CLIENT_SECRET = "GOOGLE_CLIENT_SECRET"
REDIRECT_URI = "http://127.0.0.1:8000/auth/google/callback"

# Crear instancia de GoogleSSO con los datos proporcionados
google_sso = GoogleSSO(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, REDIRECT_URI)


@router.get("/auth/google")
async def google_login():
    """
    Redirige al usuario a la página de inicio de sesión de Google.

    Returns:
        Response: Redirección a la URL de autenticación de Google.
    """
    return await google_sso.get_login_redirect()


@router.get("/auth/google/callback")
async def google_callback(request: Request):
    """
    Maneja la respuesta de Google después del inicio de sesión.

    Args:
        request (Request): La solicitud que contiene los parámetros de la respuesta de Google.

    Returns:
        HTMLResponse: Una respuesta HTML indicando el estado de la autenticación.

    Raises:
        HTTPException: Si ocurre un error durante el proceso de autenticación.
    """
    try:
        # Verificar y procesar la respuesta de Google
        user = await google_sso.verify_and_process(request)
        # Responder con un mensaje de éxito incluyendo el correo del usuario autenticado
        return HTMLResponse(f"Autenticación exitosa. Usuario: {user.email}")
    except SSOLoginError as e:
        # Manejar errores de inicio de sesión único y devolver una respuesta de error
        raise HTTPException(status_code=e.status_code, detail=e.detail)
