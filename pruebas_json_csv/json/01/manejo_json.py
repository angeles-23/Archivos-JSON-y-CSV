import os, json
os.system('cls')

"""
Python    |      JSON
dict     ➡️     Object
list     ➡️     Array
tuple    ➡️     Array
str      ➡️     String
int      ➡️     Number
float    ➡️     Number
True     ➡️     true
False    ➡️     false
None     ➡️     null
"""

'''
# Cadena JSON -> Diccionario
json_str = '{"nombre": "Oscar", "edad":28, "pais":"Perú"}'

print(json_str)
# {"nombre": "Oscar", "edad":28, "pais":"Perú"}

print(type(json_str))
# <class 'str'>


python_dict = json.loads(json_str)
print(python_dict)
# {'nombre': 'Oscar', 'edad': 28, 'pais': 'Perú'}

print(type(python_dict))
# <class 'dict'>

print(python_dict['edad'])
# 28

print(python_dict['pais'])
# Perú
'''







# DICCIONARIO -> cadena JSON
'''
data = {
    "youtuber":"Oscar24",
    "nombre":"Oscar",
    "edad":24,
    "cursos": ["PHP", "Python", "JavaScript", "C#", "Node.js"]
}

json_data = json.dumps(data)
print(json_data)
# {"youtuber": "Oscar24", "nombre": "Oscar", "edad": 24, "cursos": ["PHP", "Python", "JavaScript", "C#", "Node.js"]}

print(type(json_data))
# <class 'str'>


json_data_2 = json.dumps(data, indent=4)
print(json_data_2)
# {
#     "youtuber": "Oscar24",
#     "nombre": "Oscar",
#     "edad": 24,
#     "cursos": [
#         "PHP",
#         "Python",
#         "JavaScript",
#         "C#",
#         "Node.js"
#     ]
# }

'''

