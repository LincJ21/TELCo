from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from sso.google_sso import GoogleSSO

router = APIRouter()

# Datos proporcionados
GOOGLE_CLIENT_ID = "GOOGLE_CLIENT_ID"
GOOGLE_CLIENT_SECRET = "GOOGLE_CLIENT_SECRET"
REDIRECT_URI = "http://127.0.0.1:8000/auth/google/callback"

# Crear instancia de GoogleSSO con los datos proporcionados
google_sso = GoogleSSO(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, REDIRECT_URI)

@router.get("/auth/google")
async def google_login():
    return await google_sso.get_login_redirect()

@router.get("/auth/google/callback")
async def google_callback(request: Request):
    try:
        user = await google_sso.verify_and_process(request)
        return HTMLResponse(f"Autenticación exitosa. Usuario: {user.email}")
    except SSOLoginError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
