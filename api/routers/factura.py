from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
from datetime import datetime, timedelta

router = APIRouter()

# Datos de configuración de la base de datos
pgdatabase = 'railway'
pghost = 'monorail.proxy.rlwy.net'
pgpassword = 'ygUpKevmutHUDZWWZgaLxiBOwBkNOuUp'
pgport = '58713'
pguser = 'postgres'

def connect_db():
    return psycopg2.connect(
        dbname=pgdatabase,
        user=pguser,
        password=pgpassword,
        host=pghost,
        port=pgport
    )

class Factura(BaseModel):
    nombre: str
    cedula: str
    celular: str
    plan: str
    precio: str
    serial: str

@router.post("/guardar_factura")
async def guardar_factura(factura: Factura):
    try:
        fecha_emision = datetime.now().date()
        fecha_vencimiento = fecha_emision + timedelta(days=10)

        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO factura (nombre, cedula, celular, plan, precio, serial, fecha_emision, fecha_vencimiento)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (factura.nombre, factura.cedula, factura.celular, factura.plan, factura.precio, factura.serial, fecha_emision, fecha_vencimiento)
        )
        connection.commit()
        cursor.close()
        connection.close()

        return {"message": "Factura guardada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
