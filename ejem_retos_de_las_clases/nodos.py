'''
En estructuras de datos, un nodo es un elemento básico que se utiliza para construir otras 
estructuras más complejas, como las listas enlazadas. Un nodo generalmente contiene dos 
componentes principales: un dato y una referencia (o enlace) al siguiente nodo en la estructura.

Una lista enlazada (linked list) es una colección de nodos enlazados en secuencia. Cada nodo 
contiene un dato y un enlace al siguiente nodo en la lista. La ventaja de utilizar una lista 
enlazada es que permite la inserción y eliminación eficiente de elementos en cualquier posición, 
a diferencia de las listas o arrays que requieren reorganizar elementos.

A continuación, te muestro un ejemplo detallado de cómo implementar una lista enlazada simple 
(singly linked list) en Python:'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert(self, data, position):
        if position < 0:
            raise IndexError("Invalid position")
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while count < position - 1 and current.next is not None:
                current = current.next
                count += 1
            if current.next is None and count < position - 1:
                raise IndexError("Invalid position")
            new_node.next = current.next
            current.next = new_node

    def remove(self, data):
        if self.is_empty():
            raise ValueError("List is empty")
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None and current.next.data != data:
                current = current.next
            if current.next is None:
                raise ValueError("Data not found in list")
            current.next = current.next.next

    def display(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()


'''
En este ejemplo, la clase Node representa un nodo de la lista enlazada, 
que contiene un dato (data) y un enlace al siguiente nodo (next). 
La clase SinglyLinkedList es la lista enlazada propiamente dicha, 
que tiene un puntero a la cabeza (head) y proporciona métodos para operar en la lista.
'''