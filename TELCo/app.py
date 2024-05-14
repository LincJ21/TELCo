import fastapi
import aiofiles
import jinja2
import uvicorn
import authlib
import httpx
import itsdangerous
import psycopg2
import fastapi_sso

print("version de fastapi_sso version:", fastapi_sso.__version__)
print("Versión de FastAPI:", fastapi.__version__)
#print("Versión de aiofiles:", aiofiles.__version__)
print("Versión de Jinja2:", jinja2.__version__)
print("Versión de uvicorn:", uvicorn.__version__)
print("Versión de authlib:", authlib.__version__)
print("Versión de httpx:", httpx.__version__)
print("Versión de itsdangerous:", itsdangerous.__version__)
print("Versión de psycopg2:", psycopg2.__version__)
