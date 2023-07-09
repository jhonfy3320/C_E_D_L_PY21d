'''
Acceso a elementos: Puede acceder a los elementos de una colección utilizando índices 
(en el caso de listas y tuplas) o claves (en el caso de diccionarios). 
Por ejemplo:'''

mi_lista = [1, 2, 3]
print(mi_lista[0])  # Acceso al primer elemento de la lista: 1

mi_diccionario = {'clave': 'valor'}
print(mi_diccionario['clave'])  # Acceso al valor asociado a la clave 'clave'

'''
Modificación de elementos: Puede modificar el valor de un elemento en una colección 
utilizando su índice o clave correspondiente. Por ejemplo:'''

mi_lista = [1, 2, 3]
mi_lista[0] = 4  # Modificación del primer elemento de la lista: [4, 2, 3]

mi_diccionario = {'clave': 'valor'}
mi_diccionario['clave'] = 'nuevo_valor'  # Modificación del valor asociado a la clave 'clave'

'''Agregar elementos: Puedes agregar nuevos elementos a una colección usando métodos específicos 
según el tipo de colección. Por ejemplo:
 '''

mi_lista = [1, 2, 3]
mi_lista.append(4)  # Agregar el elemento 4 al final de la lista: [1, 2, 3, 4]

mi_diccionario = {'clave': 'valor'}
mi_diccionario['nueva_clave'] = 'nuevo_valor'  # Agregar una nueva clave-valor al diccionario

'''
Iteración: Puedes iterar sobre los elementos de una colección usando bucles como for. Por ejemplo:'''
mi_lista = [1, 2, 3]
for elemento in mi_lista:
    print(elemento)  # Imprimir cada elemento de la lista

mi_diccionario = {'clave': 'valor'}
for clave, valor in mi_diccionario.items():
    print(clave, valor)  # Imprimir cada clave y valor del diccionario

