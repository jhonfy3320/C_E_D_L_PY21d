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


# Crear una instancia de la cola:

my_queue = Queue()

#Verificar si la cola está vacía:
print(my_queue.is_empty())  # Resultado: True

#Agregar elementos a la cola:
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

#Obtener el elemento del frente de la cola:
print(my_queue.front())  # Resultado: 1

#Eliminar y obtener el elemento del frente de la cola:
print(my_queue.dequeue())  # Resultado: 1

#Obtener el tamaño actual de la cola:
print(my_queue.size())  # Resultado: 2

#Verificar si la cola está vacía nuevamente:
print(my_queue.is_empty())  # Resultado: False


'''En este ejemplo, creamos una instancia de la clase Queue llamada my_queue. 
Luego, verificamos si está vacía, agregamos elementos a la cola (1, 2 y 3), obtenemos el elemento del 
frente de la cola, eliminamos y obtenemos el elemento del frente, obtenemos el tamaño actual 
y verificamos si la cola está vacía nuevamente.

Recuerda que la cola basada en listas utiliza el método 
append() para agregar elementos al final de la lista y el método 
pop(0) para eliminar y devolver el elemento del frente de la lista.

Espero que esto te ayude a comprender cómo utilizar una cola basada en listas en Python. 
'''