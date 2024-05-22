from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from sso.google_sso import GoogleSSO  # Asegúrate de que la clase GoogleSSO esté en google_sso.py

router = APIRouter()


GOOGLE_CLIENT_ID = 'GOOGLE_CLIENT_ID'
GOOGLE_CLIENT_SECRET = 'GOOGLE_CLIENT_SECRET'

google_sso = GoogleSSO(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, "http://localhost:8000/auth/google/callback")

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
