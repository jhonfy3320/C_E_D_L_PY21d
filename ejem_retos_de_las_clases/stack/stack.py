class Stack:
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


'''
En este ejemplo, la clase Stack tiene una lista llamada items para almacenar los elementos del stack. 
Los métodos proporcionados incluyen 
is_empty() para verificar si el stack está vacío. 
push(item) para agregar un elemento en la parte superior del stack.
pop() para eliminar y devolver el elemento de la parte superior del stack. 
peek() para obtener el elemento de la parte superior sin eliminarlo. 
size() para obtener el tamaño actual del stack.

'''

#Puedes utilizar el stack de la siguiente manera:
# Crear una instancia del stack
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
