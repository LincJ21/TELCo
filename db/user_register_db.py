import psycopg2
from psycopg2 import Error

def crear_usuario(nombre, edad, email, password):
    try:
        connection = psycopg2.connect(
            dbname="telco_db",
            user="telco_db_owner",
            password="KoOWUeH2qIw6",
            host="ep-white-limit-a5bsa5ui.us-east-2.aws.neon.tech",
            sslmode="require"
        )
        
        cursor = connection.cursor()
        insert_query = "INSERT INTO usuarios (nombre, edad, email, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (nombre, edad, email, password))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except psycopg2.Error as error:
        print("Error al crear el usuario:", error)
        return False
