from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from api.routers import auth, consult, user_register
from sso.facebook import FacebookSSO
from sso.google import GoogleSSO

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Ruta para servir archivos estáticos (CSS, JavaScript, imágenes, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)
app.include_router(consult.router)
app.include_router(user_register.router)

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...), sso_provider: str = Form(...)):
    # Aquí deberías manejar la lógica de autenticación con el proveedor de SSO seleccionado
    if sso_provider == "sso_provider_1":
        # Redirigir al usuario al proveedor de SSO 1
        # Aquí deberías llamar a la lógica de autenticación de FacebookSSO
        return RedirectResponse(url=FacebookSSO().get_login_url())
    elif sso_provider == "sso_provider_2":
        # Redirigir al usuario al proveedor de SSO 2
        # Aquí deberías llamar a la lógica de autenticación de GoogleSSO
        return RedirectResponse(url=GoogleSSO().get_login_url())
    else:
        raise HTTPException(status_code=400, detail="Proveedor de SSO no válido")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})  

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/about_Carlos", response_class=HTMLResponse)
def about_Carlos(request: Request):
    return templates.TemplateResponse("about_Carlos.html", {"request": request})

@app.get("/about_Cesar", response_class=HTMLResponse)
def about_Cesar(request: Request):
    return templates.TemplateResponse("about_Cesar.html", {"request": request})

@app.get("/about_Josue", response_class=HTMLResponse)
def about_Josue(request: Request):
    return templates.TemplateResponse("about_Josue.html", {"request": request})

@app.get("/cobertura", response_class=HTMLResponse)
def cobertura(request: Request):
    return templates.TemplateResponse("cobertura.html", {"request": request})

@app.get("/servicios", response_class=HTMLResponse)
def servicios(request: Request):
    return templates.TemplateResponse("servicios.html", {"request": request})

@app.get("/base", response_class=HTMLResponse)
def base(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

if __name__ == "__app__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
