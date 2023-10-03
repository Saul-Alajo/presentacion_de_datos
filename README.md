# Prueba_final_tratamiento_de_datos

Extraer datos de la base de datos de MongoDB y presentarlos mediante Flask

### Paso 1:

Crear un archivo `.env` para confidencialidad de usuarios y contraseñas

```commandline
MONGO_USER=username # remplace con su usuario
MONGO_PASSWORD=password # remplace con su contraseña
MONGO_HOST=cluster0.patata.mongodb.net # remplace con su host
```
### Paso 2:

Instalar las librerías necesarias del archivo `requirements.txt`

```commandline
pip install -r requirements.txt
```

### Paso 3

Ejecutar `api.py`

```commandline
python3 api.py
```

## Paso 4

Chequear los resultados en http://127.0.0.1:5000 http://localhost:5000


## Esquema de ejecución
![esquema.png](Imagenes%2Fesquema.png)

