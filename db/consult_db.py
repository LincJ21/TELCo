import psycopg2
from psycopg2 import Error

def connect_to_database():
    try:
        # Establecer la conexión
        connection = psycopg2.connect(
            dbname="telco_db",
            user="telco_db_owner",
            password="KoOWUeH2qIw6",
            host="ep-white-limit-a5bsa5ui.us-east-2.aws.neon.tech",
            sslmode="require"
        )
        return connection
    except psycopg2.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

def consult_db():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ejemplo;")
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except psycopg2.Error as error:
            print("Error al ejecutar la consulta:", error)
            return None
    else:
        return None
