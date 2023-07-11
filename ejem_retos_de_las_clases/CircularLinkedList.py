class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_element(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break
            print()


'''
En esta implementación, la clase Node representa un nodo individual en la lista enlazada circular. 
Cada nodo tiene un dato (data) y un enlace al siguiente nodo (next).

La clase CircularLinkedList es la lista enlazada circular propiamente dicha. 
Tiene un puntero a la cabeza (head) y proporciona métodos para verificar si la lista está vacía, 
agregar elementos y mostrar la lista.

Para utilizar la lista enlazada circular, puedes crear una instancia de la clase CircularLinkedList 
y agregar elementos utilizando el método add_element(). Luego, puedes mostrar los elementos de la lista 
utilizando el método display().

Aquí tienes un ejemplo de uso:'''


# Crear una instancia de la lista enlazada circular
my_list = CircularLinkedList()

# Agregar elementos a la lista
my_list.add_element(1)
my_list.add_element(2)
my_list.add_element(3)

# Mostrar los elementos de la lista
my_list.display()  # Resultado: 1 2 3  (se repetirá en un ciclo infinito)

# Agregar más elementos a la lista
my_list.add_element(4)
my_list.add_element(5)

# Mostrar los elementos de la lista nuevamente
my_list.display()  # Resultado: 1 2 3 4 5  (se repetirá en un ciclo infinito)


'''
En este ejemplo, se crea una instancia de la lista enlazada circular llamada my_list 
y se agregan elementos utilizando el método add_element(). Luego, se muestra la lista utilizando 
el método display(), lo cual imprimirá los elementos de la lista en un ciclo infinito.

Recuerda que en una lista enlazada circular, el último nodo apunta de nuevo al primer nodo, formando 
un ciclo continuo.'''