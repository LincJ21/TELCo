from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from core.security.oauth import get_user_info

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    redirect_uri = request.url_for("auth")
    return templates.TemplateResponse("login.html", {"request": request, "login_url": redirect_uri})

@router.get("/auth")
async def auth(request: Request):
    user_info = await get_user_info(request)
    request.session['user_info'] = user_info
    return RedirectResponse(url="/profile")

@router.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    user_info = request.session.get('user_info')
    if user_info is None:
        raise HTTPException(status_code=401, detail="Usuario no autenticado")
    return templates.TemplateResponse("profile.html", {"request": request, "user_info": user_info})
