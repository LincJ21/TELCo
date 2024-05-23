from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
from datetime import datetime, timedelta

# Crear una instancia del enrutador de FastAPI
router = APIRouter()

# Datos de configuración de la base de datos
pgdatabase = 'railway'
pghost = 'monorail.proxy.rlwy.net'
pgpassword = 'ygUpKevmutHUDZWWZgaLxiBOwBkNOuUp'
pgport = '58713'
pguser = 'postgres'

def connect_db():
    """
    Crea y retorna una conexión a la base de datos PostgreSQL.

    Returns:
        connection (psycopg2.extensions.connection): Conexión a la base de datos.
    """
    return psycopg2.connect(
        dbname=pgdatabase,
        user=pguser,
        password=pgpassword,
        host=pghost,
        port=pgport
    )

class Factura(BaseModel):
    """
    Modelo de datos para una factura.
    """
    nombre: str
    cedula: str
    celular: str
    plan: str
    precio: str
    serial: str

@router.post("/guardar_factura")
async def guardar_factura(factura: Factura):
    """
    Guarda los datos de una factura en la base de datos.

    Args:
        factura (Factura): Datos de la factura a guardar.

    Returns:
        dict: Mensaje indicando el resultado de la operación.

    Raises:
        HTTPException: Si ocurre un error al guardar los datos en la base de datos.
    """
    try:
        # Obtener la fecha de emisión y la fecha de vencimiento
        fecha_emision = datetime.now().date()
        fecha_vencimiento = fecha_emision + timedelta(days=10)

        # Conectar a la base de datos
        connection = connect_db()
        cursor = connection.cursor()

        # Insertar los datos de la factura en la base de datos
        cursor.execute(
            """
            INSERT INTO factura (nombre, cedula, celular, plan, precio, serial, fecha_emision, fecha_vencimiento)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                factura.nombre, factura.cedula, factura.celular, 
                factura.plan, factura.precio, factura.serial, 
                fecha_emision, fecha_vencimiento
            )
        )

        # Confirmar la transacción
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        return {"message": "Factura guardada exitosamente"}
    except Exception as e:
        # Manejar cualquier excepción que ocurra y retornar un error HTTP 500
        raise HTTPException(status_code=500, detail=str(e))
