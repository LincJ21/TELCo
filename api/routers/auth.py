from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/login")
def login(username: str = Form(None), password: str = Form(None), sso_provider: str = Form(...)):
    if sso_provider == "gmail":
        return RedirectResponse(url="/auth/google")
    elif sso_provider == "facebook":
        return RedirectResponse(url="/auth/facebook")
    else:
        raise HTTPException(status_code=400, detail="Proveedor de SSO no válido")

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Otras rutas para las páginas de tu aplicación
@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@router.get("/about_Carlos", response_class=HTMLResponse)
def about_Carlos(request: Request):
    return templates.TemplateResponse("about_Carlos.html", {"request": request})

@router.get("/about_Cesar", response_class=HTMLResponse)
def about_Cesar(request: Request):
    return templates.TemplateResponse("about_Cesar.html", {"request": request})

@router.get("/about_Josue", response_class=HTMLResponse)
def about_Josue(request: Request):
    return templates.TemplateResponse("about_Josue.html", {"request": request})

@router.get("/cobertura", response_class=HTMLResponse)
def cobertura(request: Request):
    return templates.TemplateResponse("cobertura.html", {"request": request})

@router.get("/servicios", response_class=HTMLResponse)
def servicios(request: Request):
    return templates.TemplateResponse("servicios.html", {"request": request})

@router.get("/base", response_class=HTMLResponse)
def base(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
