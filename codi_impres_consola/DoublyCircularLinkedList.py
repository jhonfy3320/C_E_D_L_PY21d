# Crear una instancia de la lista doblemente enlazada circular

'''
my_list = DoublyCircularLinkedList()

# Agregar elementos a la lista
my_list.add_element(1)
my_list.add_element(2)
my_list.add_element(3)
my_list.add_element(4)
my_list.add_element(5)

# Mostrar los elementos de la lista en sentido directo
my_list.display_forward()  # Resultado: 1 2 3 4 5

# Mostrar los elementos de la lista en sentido inverso
my_list.display_backward()  # Resultado: 5 4 3 2 1

# Obtener la longitud de la lista
print(len(my_list))  # Resultado: 5

# Acceder a elementos mediante índices
print(my_list[0])  # Resultado: 1
print(my_list[2])  # Resultado: 3

# Modificar elementos mediante índices
my_list[1] = 10
print(my_list)  # Resultado: 1 10 3 4 5

# Insertar un elemento en una posición específica
my_list.insert(2, 7)
print(my_list)  # Resultado: 1 10 7 3 4 5

# Eliminar un elemento de la lista
my_list.remove(3)
print(my_list)  # Resultado: 1 10 7 4 5

# Encontrar el índice de un elemento
print(my_list.index(10))  # Resultado: 1

# Contar la cantidad de apariciones de un elemento
print(my_list.count(4))  # Resultado: 1

# Limpiar la lista
my_list.clear()
print(my_list)  # Resultado:
'''
