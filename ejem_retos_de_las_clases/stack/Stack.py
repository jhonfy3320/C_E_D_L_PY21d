class Stack:    # solucion reto de la clase 
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

    def search(self, item):
        index = self.items.index(item) if item in self.items else -1
        return index

    def traverse(self):
        for item in self.items:
            print(item, end=" ")
        print()

    def clear(self):
        self.items = []


'''
En esta implementación, la clase Stack tiene una lista llamada items para almacenar los elementos 
del stack. Los métodos incluyen is_empty() para verificar si el stack está vacío, push(item) 
para agregar un elemento en la parte superior del stack, pop() para eliminar y devolver el 
elemento de la parte superior del stack, peek() para obtener el elemento de la parte superior 
sin eliminarlo, size() para obtener el tamaño actual del stack.

Además, se agregaron los siguientes métodos según los requerimientos:

search(item): Busca un elemento en el stack y devuelve su índice. 
Si el elemento no se encuentra, devuelve -1.
traverse(): Recorre el stack e imprime los elementos en orden.
clear(): Vacía el stack, eliminando todos los elementos.
Aquí tienes un ejemplo de uso:'''


# Crear una instancia de la clase Stack
my_stack = Stack()

# Verificar si el stack está vacío
print(my_stack.is_empty())  # Resultado: True

# Agregar elementos al stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Obtener el elemento de la parte superior del stack
print(my_stack.peek())  # Resultado: 3

# Eliminar y obtener el elemento de la parte superior del stack
print(my_stack.pop())  # Resultado: 3

# Obtener el tamaño actual del stack
print(my_stack.size())  # Resultado: 2

# Buscar un elemento en el stack
print(my_stack.search(2))  # Resultado: 1

# Recorrer el stack
my_stack.traverse()  # Resultado: 1 2

# Vaciar el stack
my_stack.clear()
print(my_stack.is_empty())  # Resultado: True


# nota 
'''
itando a SoloLearn, datos curiosos de Python:
Según el creador Guido Van Rossum, el nombre de Python viene de la serie de comedia británica 
“El circo Volador de Monty Python”.
Es por ello que se usan “spam” y “eggs”, haciendo referencia al grupo de comedia.
Les dejo un video donde repiten esas palabras 😄'''