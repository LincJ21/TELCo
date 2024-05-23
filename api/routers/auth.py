from fastapi import APIRouter, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer
import requests

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Definir la URL de autorización de Google OAuth
GOOGLE_AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/auth"

@router.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...), sso_provider: str = Form(...)):
    if sso_provider == "gmail":
        return RedirectResponse(url="/auth/google")
    else:
        raise HTTPException(status_code=400, detail="Proveedor de SSO no válido")

@router.get("/auth/google")
async def google_login():
    # Construir la URL de autorización de Google OAuth
    authorization_url = f"{GOOGLE_AUTHORIZATION_URL}?response_type=code&client_id=678574468316-vas8o20hvo8l10ee6ffs9ln3g8kdnm54.apps.googleusercontent.com&redirect_uri=http://127.0.0.1:8000/auth/google/callback&scope=email%20profile"
    return RedirectResponse(url=authorization_url)

@router.get("/auth/google/callback")
async def google_callback(request: Request, code: str, oauth2_scheme: OAuth2AuthorizationCodeBearer = Depends()):
    data = {
        "code": code,
        "GOOGLE_CLIENT_ID": "GOOGLE_CLIENT_ID",
        "GOOGLE_CLIENT_SECRET": "GOOGLE_CLIENT_SECRET",
        "redirect_uri": "http://127.0.0.1:8000/auth/google/callback",
        "grant_type": "authorization_code",
    }
    response = requests.post(oauth2_scheme.tokenUrl, data=data)
    access_token = response.json().get("access_token")
    # Usar el access_token para obtener información del usuario u otras acciones
    return {"access_token": access_token}

@router.get('/welcome')
def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})
# Resto de las rutas y funciones

@router.route('/comprarP', methods=['GET', 'POST'])
async def comprar(request: Request):
    if request.method == 'POST':
        # Procesar la información del formulario si es una solicitud POST
        form_data = await request.form()
        cc = form_data['cc']
        nombre = form_data['nombre']
        apellido = form_data['apellido']
        email = form_data['email']
        departamento = form_data['departamento']
        ciudad_pueblo = form_data['ciudad_pueblo']
        barrio = form_data['barrio']
        celular = form_data['celular']
        numero_tarjeta = form_data['numero_tarjeta']
        fecha_expiracion = form_data['fecha_expiracion']
        codigo_seguridad = form_data['codigo_seguridad']
        contraseña = form_data['contraseña']
        plan_referencia = form_data['plan_referencia']
        #guardar_compra(cc, nombre, apellido, email, departamento, ciudad_pueblo, barrio, celular, numero_tarjeta, fecha_expiracion, codigo_seguridad, contraseña)
        #clasificar(cc, plan_referencia)
        return templates.TemplateResponse("comprar.html", {"request": request, "error": None, "success": "Compra registrada exitosamente"})

    elif request.method == 'GET':
        # Manejar la lógica si es una solicitud GET
        plan_referencia = request.query_params.get('plan_referencia')
        return templates.TemplateResponse("comprar.html", {"request": request, "error": None, "success": None, "plan_referencia": plan_referencia})

    # Manejar otras situaciones
    return templates.TemplateResponse("comprar.html", {"request": request, "error": "Error desconocido", "success": None, "plan_referencia": None})

@router.get("/contratar")
def contratar(request: Request):
    return templates.TemplateResponse("contratar.html", {"request": request})
@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

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

@router.get("/user_register", response_class=HTMLResponse)
def user_register(request: Request):
    return templates.TemplateResponse("user_register.html", {"request": request})

@router.get("/entretenimiento", response_class=HTMLResponse)
def entretenimiento(request: Request):
    return templates.TemplateResponse("entretenimiento.html", {"request": request})

@router.get("/internet", response_class=HTMLResponse)
def internet(request: Request):
    return templates.TemplateResponse("internet.html", {"request": request})

@router.get("/familiar", response_class=HTMLResponse)
def familiar(request: Request):
    return templates.TemplateResponse("familiar.html", {"request": request})