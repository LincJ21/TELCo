import psycopg2
from psycopg2 import Error

try:
    # Establecer la conexión
    connection = psycopg2.connect(
        dbname="telco_db",
        user="telco_db_owner",
        password="KoOWUeH2qIw6",
        host="ep-white-limit-a5bsa5ui.us-east-2.aws.neon.tech",
        sslmode="require"
    )

    # Crear un cursor
    cursor = connection.cursor()

    # Crear una tabla de ejemplo
    create_table_query = '''
    CREATE TABLE ejemplo (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        edad INT
    );
    '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Tabla creada correctamente.")

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error al conectar a la base de datos:", error)
