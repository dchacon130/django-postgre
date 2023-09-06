# Usa la imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el contenido de la aplicación al contenedor
COPY . /app/