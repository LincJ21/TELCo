# Usa una imagen base de Python
FROM python:3.11.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /TELCo

# Copia los archivos de tu aplicación
COPY . .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación FastAPI se ejecuta
EXPOSE 8000

# Comando de inicio de la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
