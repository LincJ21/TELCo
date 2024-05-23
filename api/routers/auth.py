from fastapi import APIRouter, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer
import requests

# Crear una instancia del enrutador de FastAPI
router = APIRouter()
# Configurar Jinja2Templates con el directorio de plantillas
templates = Jinja2Templates(directory="templates")

# Definir la URL de autorización de Google OAuth
GOOGLE_AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/auth"

@router.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...), sso_provider: str = Form(...)):
    """
    Endpoint para iniciar sesión utilizando un formulario.
    
    Args:
        request (Request): La solicitud HTTP.
        username (str): Nombre de usuario proporcionado en el formulario.
        password (str): Contraseña proporcionada en el formulario.
        sso_provider (str): Proveedor de SSO (por ejemplo, 'gmail').

    Returns:
        RedirectResponse: Redirección a la URL de autenticación de Google si sso_provider es 'gmail'.
    
    Raises:
        HTTPException: Si el proveedor de SSO no es válido.
    """
    if sso_provider == "gmail":
        return RedirectResponse(url="/auth/google")
    else:
        raise HTTPException(status_code=400, detail="Proveedor de SSO no válido")

@router.get("/auth/google")
async def google_login():
    """
    Endpoint para iniciar el proceso de autenticación con Google OAuth.
    
    Returns:
        RedirectResponse: Redirección a la URL de autorización de Google OAuth.
    """
    authorization_url = (
        f"{GOOGLE_AUTHORIZATION_URL}?response_type=code"
        "&client_id=678574468316-vas8o20hvo8l10ee6ffs9ln3g8kdnm54.apps.googleusercontent.com"
        "&redirect_uri=http://127.0.0.1:8000/auth/google/callback"
        "&scope=email%20profile"
    )
    return RedirectResponse(url=authorization_url)

@router.get("/auth/google/callback")
async def google_callback(request: Request, code: str, oauth2_scheme: OAuth2AuthorizationCodeBearer = Depends()):
    """
    Endpoint de callback para manejar la respuesta de Google OAuth.
    
    Args:
        request (Request): La solicitud HTTP.
        code (str): Código de autorización proporcionado por Google OAuth.
        oauth2_scheme (OAuth2AuthorizationCodeBearer): Esquema de autorización de OAuth2.

    Returns:
        dict: Diccionario con el token de acceso.
    """
    data = {
        "code": code,
        "client_id": "GOOGLE_CLIENT_ID",
        "client_secret": "GOOGLE_CLIENT_SECRET",
        "redirect_uri": "http://127.0.0.1:8000/auth/google/callback",
        "grant_type": "authorization_code",
    }
    response = requests.post(oauth2_scheme.tokenUrl, data=data)
    access_token = response.json().get("access_token")
    return {"access_token": access_token}

@router.get('/welcome')
def welcome(request: Request):
    """
    Endpoint para mostrar la página de bienvenida.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'welcome.html'.
    """
    return templates.TemplateResponse("welcome.html", {"request": request})

@router.route('/comprarP', methods=['GET', 'POST'])
async def comprar(request: Request):
    """
    Endpoint para manejar la compra de productos.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'comprar.html'.
    """
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
    """
    Endpoint para mostrar la página de contratación de servicios.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'contratar.html'.
    """
    return templates.TemplateResponse("contratar.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    """
    Endpoint para mostrar la página de inicio de sesión.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'login.html'.
    """
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    """
    Endpoint para mostrar la página de inicio.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'home.html'.
    """
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/about", response_class=HTMLResponse)
def about(request: Request):
    """
    Endpoint para mostrar la página 'Sobre nosotros'.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'about.html'.
    """
    return templates.TemplateResponse("about.html", {"request": request})

@router.get("/about_Carlos", response_class=HTMLResponse)
def about_Carlos(request: Request):
    """
    Endpoint para mostrar la página 'Sobre Carlos'.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'about_Carlos.html'.
    """
    return templates.TemplateResponse("about_Carlos.html", {"request": request})

@router.get("/about_Cesar", response_class=HTMLResponse)
def about_Cesar(request: Request):
    """
    Endpoint para mostrar la página 'Sobre Cesar'.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'about_Cesar.html'.
    """
    return templates.TemplateResponse("about_Cesar.html", {"request": request})

@router.get("/about_Josue", response_class=HTMLResponse)
def about_Josue(request: Request):
    """
    Endpoint para mostrar la página 'Sobre Josue'.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'about_Josue.html'.
    """
    return templates.TemplateResponse("about_Josue.html", {"request": request})

@router.get("/cobertura", response_class=HTMLResponse)
def cobertura(request: Request):
    """
    Endpoint para mostrar la página de cobertura.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'cobertura.html'.
    """
    return templates.TemplateResponse("cobertura.html", {"request": request})

@router.get("/servicios", response_class=HTMLResponse)
def servicios(request: Request):
    """
    Endpoint para mostrar la página de servicios.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'servicios.html'.
    """
    return templates.TemplateResponse("servicios.html", {"request": request})

@router.get("/base", response_class=HTMLResponse)
def base(request: Request):
    """
    Endpoint para mostrar la plantilla base.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'base.html'.
    """
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/home", response_class=HTMLResponse)
def home(request: Request):
    """
    Endpoint para mostrar la página de inicio.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'home.html'.
    """
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/user_register", response_class=HTMLResponse)
def user_register(request: Request):
    """
    Endpoint para mostrar la página de registro de usuarios.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'user_register.html'.
    """
    return templates.TemplateResponse("user_register.html", {"request": request})

@router.get("/entretenimiento", response_class=HTMLResponse)
def entretenimiento(request: Request):
    """
    Endpoint para mostrar la página de entretenimiento.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'entretenimiento.html'.
    """
    return templates.TemplateResponse("entretenimiento.html", {"request": request})

@router.get("/internet", response_class=HTMLResponse)
def internet(request: Request):
    """
    Endpoint para mostrar la página de servicios de internet.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'internet.html'.
    """
    return templates.TemplateResponse("internet.html", {"request": request})

@router.get("/familiar", response_class=HTMLResponse)
def familiar(request: Request):
    """
    Endpoint para mostrar la página de servicios familiares.

    Args:
        request (Request): La solicitud HTTP.

    Returns:
        TemplateResponse: Respuesta de la plantilla 'familiar.html'.
    """
    return templates.TemplateResponse("familiar.html", {"request": request})
