class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_element(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            current = self.head.prev
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node

    def display_forward(self):
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

    def display_backward(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head.prev
            while True:
                print(current.data, end=" ")
                current = current.prev
                if current == self.head.prev:
                    break
            print()

    def __len__(self):
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value

    def insert(self, index, data):
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        if index == 0:
            self.add_element(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def remove(self, data):
        if self.is_empty():
            raise ValueError("List is empty")
        current = self.head
        while True:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                del current
                break
            current = current.next
            if current == self.head:
                raise ValueError("Data not found in list")

    def index(self, data):
        current = self.head
        index = 0
        while True:
            if current.data == data:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        raise ValueError("Data not found in list")

    def count(self, data):
        count = 0
        current = self.head
        while True:
            if current.data == data:
                count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def clear(self):
        while not self.is_empty():
            self.remove(self.head.data)

'''
 Node representa un nodo individual en la lista doblemente enlazada circular. 
 Cada nodo tiene un dato (data), 
 un enlace al nodo anterior (prev) y un enlace al nodo siguiente (next).

La clase DoublyCircularLinkedList es la lista doblemente enlazada circular propiamente dicha. 
Tiene un puntero a la cabeza 
(head) y proporciona métodos para verificar si la lista está vacía, 
agregar elementos, mostrar la lista en sentido directo 
(display_forward()) y en sentido inverso 
(display_backward()), y operaciones adicionales como obtener la longitud 
(__len__()), acceder a elementos mediante índices 
(__getitem__() y __setitem__()), insertar elementos en una posición específica 
(insert()), eliminar elementos (remove()), encontrar el índice de un elemento 
(index()), contar la cantidad de apariciones de un elemento 
(count()), y limpiar la lista (clear()).

Puedes utilizar estos métodos para interactuar con la lista doblemente enlazada circular. 
Aquí tienes un ejemplo de uso:
ir a la carpeta code_impres_consola archivo con extención py DoublyCircularLinkedList'''