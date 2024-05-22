import psycopg2

# Datos de configuración
pgdatabase = 'railway'
pghost = 'monorail.proxy.rlwy.net'
pgpassword = 'ygUpKevmutHUDZWWZgaLxiBOwBkNOuUp'
pgport = '58713'
pguser = 'postgres'

try:
    # Establecer la conexión a la base de datos
    connection = psycopg2.connect(
        dbname=pgdatabase,
        user=pguser,
        password=pgpassword,
        host=pghost,
        port=pgport
    )
    print("Conexión establecida")

    # Crear un cursor
    cursor = connection.cursor()

    # Modificar la definición de la tabla factura
    query = """
    ALTER TABLE factura
    ALTER COLUMN precio TYPE NUMERIC(10, 2);
    """
    cursor.execute(query)

    # Confirmar la transacción
    connection.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()
    print("Modificación completada en la tabla 'factura'")

except Exception as e:
    print(f"Error al realizar la consulta: {e}")

