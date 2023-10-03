# Prueba_final_tratamiento_de_datos

Extraer datos de los equipos de la página https://mikrotik.com, almacenarlos en una base de datos y visualizar mediante Flask

### Paso 1:

Crear un archivo `.env` para confidencialidad de usuarios y contraseñas

```commandline
MONGO_USER=username # remplace con su usuario
MONGO_PASSWORD=password # remplace con su contraseña
MONGO_HOST=cluster0.patata.mongodb.net # remplace con su host
```
### Paso 2:

Instalar las librerías necesarias

```commandline
pip install -r requirements
```

### Paso 3

Ejecutar `main.py`

```commandline
python3 main.py
```

## Paso 4

Chequear los resultados en MongoDB
![img.png](Imagenes/img.png)

## Esquema de ejecución
![img.png](Imagenes/ESQUEMA.png)

