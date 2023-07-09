from array import array as Array


class Cube:
    def __init__(self, rows, columns, depth, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)
            for column in range(columns):
                self.data[row][column] = Array(depth, fill_value)

    def populate(self, value):
        for row in range(len(self.data)):
            for column in range(len(self.data[row])):
                for depth in range(len(self.data[row][column])):
                    self.data[row][column][depth] = value

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def get_depth(self):
        return len(self.data[0][0])

    def __getitem__(self, index):
        return self.data[index]

'''my_cube = Cube(2, 2, 2)
my_cube.populate(1)

print(my_cube.data)  # Imprimir slots del cubo
print(my_cube.get_height())  # Obtener la altura del cubo
print(my_cube.get_width())  # Obtener el ancho del cubo
print(my_cube.get_depth())  # Obtener la profundidad del cubo
'''