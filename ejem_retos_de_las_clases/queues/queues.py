class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

'''
En este ejemplo, la clase Queue tiene una lista llamada items para almacenar los elementos de la cola. 
Los métodos proporcionados incluyen 
is_empty() para verificar si la cola está vacía.
enqueue(item) para agregar un elemento al final de la cola.
dequeue() para eliminar y devolver el elemento del frente de la cola.
front() para obtener el elemento del frente sin eliminarlo.
rear() para obtener el elemento del final sin modificar la cola.
size() para obtener el tamaño actual de la cola.'''

# Crear una instancia de la cola
my_queue = Queue()

# Verificar si la cola está vacía
print(my_queue.is_empty())  # Resultado: True

# Agregar elementos a la cola
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# Obtener el elemento del frente de la cola
print(my_queue.front())  # Resultado: 1

# Eliminar y obtener el elemento del frente de la cola
print(my_queue.dequeue())  # Resultado: 1

# Obtener el tamaño actual de la cola
print(my_queue.size())  # Resultado: 2

# Verificar si la cola está vacía nuevamente
print(my_queue.is_empty())  # Resultado: False