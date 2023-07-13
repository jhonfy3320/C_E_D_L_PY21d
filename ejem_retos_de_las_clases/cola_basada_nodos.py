class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return item

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.front.data

    def size(self):
        count = 0
        current = self.front

        while current:
            count += 1
            current = current.next

        return count

'''En esta implementación, utilizamos la clase Nodepara representar los nodos individuales en la cola. 
Luego, la clase Queuetiene un puntero al frente ( front) y un puntero al final ( rear) de la cola.

El metodois_empty() verifica si la cola esta vacia.
El método enqueue(item)agrega un elemento al final de la cola creando un nuevo nodo y actualizando el punterorear .
El método dequeue()elimina y devuelve el elemento del frente de la cola, actualizando el puntero front.
El metodo front()devuelve el elemento del frente de la cola sin eliminarlo.
El método size()devuelve el tamaño real de la cola contando los nudos.'''
#Puedes utilizar la cola basada en nudos de la siguiente manera:

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


'''La cola basada en nodos es útil cuando se requiere una estructura de datos dinámicos para administrar 
elementos en orden de llegada. 
Se utiliza en situaciones donde se necesita procesar elementos de manera secuencial y respetando el principio
FIFO (First In, First Out), como en colas de procesamiento de tareas, sistemas de planificación y 
gestión de solicitudes.'''