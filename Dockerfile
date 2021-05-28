FROM python:3.8.10-buster
#/alternativa 3.10.0b1-buster

# hacer directorio para la aplicacion

WORKDIR /App

# instalar dependencias

COPY requeriments.txt .
RUN pip install -r requeriments.txt

# Copiar el codigo

COPY /App .

# Correr App

CMD ["python", "App.py"]