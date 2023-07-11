class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_element(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

    def display_backward(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data, end=" ")
                current = current.prev
            print()


'''
n esta implementación, la clase Node representa un nodo individual en la lista doblemente enlazada. 
Cada nodo tiene un dato (data), un enlace al nodo anterior (prev) y un enlace al nodo siguiente (next).

La clase DoublyLinkedList es la lista doblemente enlazada propiamente dicha. 
Tiene un puntero a la cabeza 
(head) y proporciona métodos para verificar si la lista está vacía, 
agregar elementos y mostrar la lista en sentido directo 
(display_forward()) o en sentido inverso (display_backward()).

Para utilizar la lista doblemente enlazada, puedes crear una instancia de la clase 
DoublyLinkedList y agregar elementos utilizando el método 
add_element(). Luego, puedes mostrar los elementos de la lista utilizando los métodos 
display_forward() o display_backward().

'''
#Aquí tienes un ejemplo de uso:
# Crear una instancia de la lista doblemente enlazada
my_list = DoublyLinkedList()

# Agregar elementos a la lista
my_list.add_element(1)
my_list.add_element(2)
my_list.add_element(3)

# Mostrar los elementos de la lista en sentido directo
my_list.display_forward()  # Resultado: 1 2 3

# Mostrar los elementos de la lista en sentido inverso
my_list.display_backward()  # Resultado: 3 2 1

'''En este ejemplo, se crea una instancia de la lista doblemente enlazada llamada 
my_list y se agregan elementos utilizando el método 
add_element(). Luego, se muestra la lista en sentido directo utilizando el método 
display_forward(), que imprimirá los elementos de la lista en el orden en que se agregaron. 
Luego, se muestra la lista en sentido inverso utilizando el método 
display_backward(), que imprimirá los elementos de la lista en orden inverso.

La lista doblemente enlazada permite el recorrido en ambos sentidos, ya que cada nodo tiene enlaces 
tanto al nodo anterior como al siguiente. 
Esto permite operaciones más eficientes para insertar, eliminar y acceder a elementos en diferentes 
posiciones de la lista.'''