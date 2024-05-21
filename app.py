from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.routers import auth, google_sso, facebook_sso

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Ruta para servir archivos estáticos (CSS, JavaScript, imágenes, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir routers
app.include_router(auth.router)
app.include_router(google_sso.router)
app.include_router(facebook_sso.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
