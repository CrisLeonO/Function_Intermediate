# 1. Actualizar valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1] = [15, 8, 9]
print(x[1])

# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Bryant'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
print(estudiantes)

# En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Andres', 'Ronaldo', 'Rooney']
}
print(directorio_deportes)

# Cambia el valor 20 en z a 30.
z = [{'x': 10, 'y': 30}]

print(z[0])

print('*' * 40)
# segundo punto --------------------------------------------------------------------------------------------------------------
''''Iterar a través de una lista de diccionarios
Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:'''
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary():
    for x in estudiantes:
        print('first_name -', x['first_name'],
              ',', 'last_name - ', x['last_name'])


iterateDictionary()
print('*' * 40)
# 3er punto ----------------------------------------------------------------------------------------------------------------------------
'''Obtener valores de una lista de diccionarios
Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:'''

names = {
    'name1': 'Michael',
    'name2': 'John',
    'name3': 'Mark',
    'name4': 'KB'
}
estudiantes = {
    'last_name1': 'Jordan',
    'last_name2': 'Rosales',
    'last_name3': 'Guillen',
    'last_name4': 'Tonel'
}


def iterateDictionary2(names):
    for val in names.values():
        print(val)


iterateDictionary2(names)

print('*' * 20)


def iterateDictionary2(estudiantes):
    for x in estudiantes.values():
        print(x)


iterateDictionary2(estudiantes)
print('*' * 20)

# 4to punto
'''Iterar a través de un diccionarios con valores de lista
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:'''

dojo = {
    "ubicaciones": ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    "instructores": ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon', 'Jorge'],
}


def printInfo(dojo):
    for x, valor in dojo.items():
        print(len(dojo[x]), x)
        print(*valor, sep='\n')


printInfo(dojo)
