from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi_sso.sso.google import GoogleSSO

router = APIRouter()

GOOGLE_CLIENT_ID = "TU_GOOGLE_CLIENT_ID"
GOOGLE_CLIENT_SECRET = "TU_GOOGLE_CLIENT_SECRET"

google_sso = GoogleSSO(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, "http://localhost:8000/auth/google/callback")

@router.get("/auth/google")
async def google_login():
    return await google_sso.get_login_redirect()

@router.get("/auth/google/callback")
async def google_callback(request: Request):
    user = await google_sso.verify_and_process(request)
    if user:
        return HTMLResponse(f"Autenticación exitosa. Usuario: {user.email}")
    raise HTTPException(status_code=400, detail="Error en la autenticación de Google")
