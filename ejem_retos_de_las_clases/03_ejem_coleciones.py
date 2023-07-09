'''
Listas (Lists): Las listas son colecciones ordenadas y modificables de elementos. 
Puede almacenar cualquier tipo de datos en una lista y acceder a ellos mediante índices. Por ejemplo:'''

mi_lista = [1, 2, 3,4,5,6,7,8,9,0, 'cuatro', 'cinco','freddy','emanuel','nico','alejandro']

'''
Tuplas (Tuples): Las tuplas son colecciones ordenadas e inmutables de elementos. 
Son similares a las listas, pero no se pueden modificar después de su creación. Por ejemplo:'''

mi_tupla = (11, 12, 13,14,15,16,17,18,19,20, 'cuatro', 'cinco','freddy','emanuel','nico','alejandro')

'''Conjuntos (Sets): Los conjuntos son colecciones no ordenadas de elementos únicos. 
Los elementos en un conjunto no tienen un orden específico y no se pueden duplicar. 
Los conjuntos son útiles para eliminar duplicados y realizar operaciones de conjuntos como unión, 
intersección, etc. Por ejemplo:'''

mi_conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0} #conjunto 

'''Diccionarios (Dictionaries): Los diccionarios son colecciones no ordenadas de pares clave-valor. 
Los elementos se almacenan y acceden mediante una clave en lugar de un índice. 
Los diccionarios son útiles cuando necesitan almacenar datos en forma de pares clave-valor y 
realizar búsquedas rápidas por clave. Por ejemplo:'''

mi_diccionario = {
    'nombre': 'Juan', 
    'edad': 30, 
    'ciudad': 'Madrid'
    
    }

print(mi_lista, 
      mi_tupla,
      mi_conjunto,
      mi_diccionario)

'''
Estas son solo algunas de las colecciones construidas en Python. 
Cada una tiene características y funcionalidades específicas que las hacen útiles en diferentes 
situaciones. '''