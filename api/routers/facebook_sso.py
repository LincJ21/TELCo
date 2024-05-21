from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi_sso.sso.facebook import FacebookSSO

router = APIRouter()

FACEBOOK_CLIENT_ID = "TU_FACEBOOK_CLIENT_ID"
FACEBOOK_CLIENT_SECRET = "TU_FACEBOOK_CLIENT_SECRET"

facebook_sso = FacebookSSO(FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET, "http://localhost:8000/auth/facebook/callback")

@router.get("/auth/facebook")
async def facebook_login():
    return await facebook_sso.get_login_redirect()

@router.get("/auth/facebook/callback")
async def facebook_callback(request: Request):
    user = await facebook_sso.verify_and_process(request)
    if user:
        return HTMLResponse(f"Autenticación exitosa. Usuario: {user.email}")
    raise HTTPException(status_code=400, detail="Error en la autenticación de Facebook")
