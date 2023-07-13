class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def is_empty(self):
        return len(self.inbound_stack) == 0 and len(self.outbound_stack) == 0

    def enqueue(self, item):
        self.inbound_stack.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        if len(self.outbound_stack) == 0:
            while len(self.inbound_stack) > 0:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop()

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        if len(self.outbound_stack) == 0:
            while len(self.inbound_stack) > 0:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack[-1]

    def size(self):
        return len(self.inbound_stack) + len(self.outbound_stack)


'''
En esta implementación, utilizamos dos stacks: inbound_stackpara agregar (agregar elementos) y `outbound_stackoutbound_stackpara desencolar (eliminar elementos).

El método is_empty()verifica si ambas pilas están vacías.
El metodo enqueue(item)agregainbound_stack.
El metodo dequeue()extrae youtbound_stack. Si la pila 
outbound_stackestá vacía, transferimos los elementos 
delinbound_stackal outbound_stacken orden inverso antes de realizar la operación de desencolar.
El metodo `front()devuelve el elemento del frente del stack outbound_stacksin eliminarlo. 
Si el stack outbound_stackestá vacío, transferimos los elementos del 
`ininbound_stack al outbound_stacken orden inverso antes de obtener el elemento del frente.
El método size()devuelve el tamaño total de la cola.
Puedes utilizar la'''

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
