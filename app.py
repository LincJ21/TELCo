import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.routers import auth, google_sso, facebook_sso
from sso.google_sso import GoogleSSO
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer  # Importa la clase OAuth2AuthorizationCodeBearer


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Definir OAuth2AuthorizationCodeBearer
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://accounts.google.com/o/oauth2/auth",
    tokenUrl="https://oauth2.googleapis.com/token",
)

# Crear instancia de GoogleSSO con los valores de client_id y client_secret
google_sso_instance = GoogleSSO(
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET")
)

# Incluir la instancia de GoogleSSO en tu enrutador de autenticación
auth.google_sso = google_sso_instance

app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir routers
app.include_router(auth.router)
app.include_router(google_sso.router)
app.include_router(facebook_sso.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
