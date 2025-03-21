# JSON en Python

### Sintáxis JSON
JSON representa datos de forma **clave-valor**, parecido a los diccionarios en Python:

``` json
{
    "nombre": "Santiago",
    "edad": 25,
    "activo": true,
    "hobbies": ["fútbol","escuchar música"],
    "direccion": {
        "calle": "Av. Juan Carlos I",
        "ciudad":"Lorca"
    }
}
```

- Las claves deben estar entre comillas dobles
- Los valores pueden ser cadenas, números, boolean, listas u otros objetos JSON



### Manipulación de JSON en Python
Se debe importar la libreríajson: `import json`

| Función | Descripción |
|---------|-------------|
|Trabajar con archivos JSON|
|**`json.load(f)`**|Leer un archivo JSON ➡️ diccionario|
|**`json.dump(obj, f)`** |Escribir y guardar un diccionario ➡️ JSON con indent=4|
|Trabajar con datos JSON en forma de cadena|
|**`json.loads(s)`**|Leer cadenas JSON ➡️ diccionario|
|**`json.dumps(obj)`**|Diccionarios ➡️ cadenas JSON con indent=4|


### Ejemplo `json.loads()`
#### 1. Dentro del código
``` python
import json

# Cadena JSON
datos_json = '{"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}'

# Convertir la cadena JSON a un diccionario de Python
datos = json.loads(datos_json)
print(datos)
```

**Resultado:**
```python
{'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
```

**Explcación:**
- `import json`:  importa el módulo json en Python. Proporciona funciones para trabajar con datos en formato JSON
- `datos_json = '{"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}'`: 
  - `json.loads()`: convierte la cadena datos_json a un diccionario
- `print(datos)`: imprime los datos



#### 2. JSON fuera del código
datos.json
``` json
{
  "nombre": "Juan",
  "edad": 30,
  "ciudad": "Madrid"
}
```

ejercicio. py
``` python
import json
# Abrir el archivo y cargar el contenido JSON

with open('datos.json', 'r') as f:
    datos = json.load(f) # Usamos json.load() cuando leemos un archivo

print(datos)
```

**Resultado:**
``` python
{'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
```

**Explcación:**
- `import json`: importa el módulo json en Python.
-  `with open('datos.json', 'r') as f`: abrimos el archivo 'datos.json' en modo lectura 'r'.
   - `datos = json.load(f)`: lee el contenido del archivo f y lo convierte en un diccionario.
- `print(datos)`: imprime los datos







### Ejemplo `json.dumps()`
``` python
import json

# Diccionario de Python
datos_python = {
    "nombre": "Ana",
    "edad": 30,
    "activo": True,
    "ciudad": "Barcelona"
}

# Convertir el diccionario a JSON
datos_json = json.dumps(datos_python)
datos_json_con_formato = json.dumps(datos_python, indent=4)
print(datos_json)
print(datos_json_con_formato)
```

**Resultado**:
```python
{"nombre": "Ana", "edad": 30, "activo": true, "ciudad": "Barcelona"}

# Con formato indent=4
{
    "nombre": "Ana",
    "edad": 30,
    "activo": true,
    "ciudad": "Barcelona"
}
```

**Explicación**:
- `datos_python`: es un diccionario en Python
- `json.dumps()`: convierte el diccionario en una cadena JSON
- `print(datos_json)`: imprime el diccionario






### Leer y Escribir Archivos JSON
Con las funciones `json.load()` y `json.dump()`

#### Leer un Archivo JSON
```python
import json

# Abrir el archivo JSON
with open('datos.json', 'r') as f:
    python_datos = json.load(f)

print(python_datos)
```

**Resultado:**
```python
{'nombre': 'Alba', 'edad': 25, 'ciudad': 'Valencia'}
```

**Explicación**:
- `json.load()`: lee el archivo JSON y lo convierte en un diccionario o lista de Python



#### Escribir un Archivo JSON
```python
import json

datos_python = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Sevilla"
}

# Escribir los datos en un archivo JSON
with open('salida.json', 'w') as f:
    contenido = json.dump(datos_python, f, indent=4)
```

**Explicación**:
- `json.dump()`: escribe el contenido del diccionario datos_python en un archivo JSON

