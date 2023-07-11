class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
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

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __contains__(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, index, data):
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, data):
        if not self.head:
            raise ValueError("List is empty")
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next and current.next.data != data:
                current = current.next
            if not current.next:
                raise ValueError("Data not found in list")
            current.next = current.next.next

    def index(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        raise ValueError("Data not found in list")

    def count(self, data):
        count = 0
        current = self.head
        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count

    def clear(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def copy(self):
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        if index == 0:
            data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            data = current.next.data
            current.next = current.next.next
        return data

    def __str__(self):
        return '[' + ', '.join(str(item) for item in self) + ']'

'''
Esta implementación de la lista enlazada (LinkedList) incluye los siguientes métodos:

__len__(): Devuelve la longitud de la lista.
__getitem__(index): Permite acceder a los elementos de la lista mediante índices.
__setitem__(index, value): Permite modificar los elementos de la lista mediante índices.
__iter__(): Permite iterar sobre los elementos de la lista.
__contains__(value): Verifica si un valor está presente en la lista.
append(data): Agrega un elemento al final de la lista.
insert(index, data): Inserte un elemento en una posición específica de la lista.
remove(data): Elimina la primera aparición de un elemento de la lista.
index(data): Devuelve el índice de la primera aparición de un elemento en la lista.
count(data): Cuenta la cantidad de apariciones de un elemento en la lista.
clear(): Elimina todos los elementos de la lista.
reverse(): Invierte el orden de los elementos en la lista.
copy(): Crea una copia de la lista.
extend(iterable): Agrega los elementos de un iterable al final de la lista.
pop(index=None): Elimina y devuelve el elemento en la posición especificada o el último elemento si no se proporciona un índice.
__str__(): Devuelve una representación en cadena de la lista.
Estos métodos te permitirán utilizar la lista enlazada de manera similar a una lista estándar de Python.

Espero que esta implementación sea útil.'''