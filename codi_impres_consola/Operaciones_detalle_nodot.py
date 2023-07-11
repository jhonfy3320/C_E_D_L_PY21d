'''
Para ejecutar el código que proporcionaste, puedes seguir estos pasos:

Abre tu entorno de desarrollo de Python, como IDLE o un editor de código como VS Code.
Crea un nuevo archivo de Python y copia el código en él.
Guarda el archivo con un nombre y una extensión ".py", por ejemplo, "linked_list.py".
Ejecuta el archivo haciendo clic en el botón de ejecución o utilizando el comando adecuado en tu entorno 
de desarrollo. 
También puedes ejecutarlo desde la línea de comandos usando el comando python linked_list.py, 
asumiendo que tienes Python instalado correctamente en tu sistema.
Una vez que ejecuta el archivo, el código definirá las clases Nodey LinkedList, junto con todos los 
métodos y atributos asociados. No verá ninguna salida en la consola a menos que agregue instrucciones 
para usar y probar la lista enlazada.

Puede utilizar los métodos de la clase LinkedListpara realizar diferentes operaciones en la lista 
enlazada, como agregar elementos, eliminar elementos, obtener la longitud, etc. Por ejemplo, 
puede agregar el siguiente código al final del archivo para probar la lista enlazada:'''


'''# Crear una instancia de la lista enlazada
my_list = LinkedList()

# Agregar elementos a la lista
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Mostrar la lista enlazada
print(my_list)  # Resultado: [1, 2, 3]

# Obtener la longitud de la lista
print(len(my_list))  # Resultado: 3

# Acceder a elementos mediante índices
print(my_list[0])  # Resultado: 1
print(my_list[2])  # Resultado: 3

# Modificar elementos mediante índices
my_list[1] = 4
print(my_list)  # Resultado: [1, 4, 3]

# Eliminar un elemento de la lista
my_list.remove(4)
print(my_list)  # Resultado: [1, 3]'''