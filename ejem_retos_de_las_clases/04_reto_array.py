import random

class MiArray:
    def __init__(self, size):
        self.size = size
        self.slots = []

    def poblar_aleatorio(self, limite):
        self.slots = [random.randint(0, limite) for _ in range(self.size)]

    def poblar_secuencial(self):
        self.slots = [i+1 for i in range(self.size)]

    def sumar_valores(self):
        return sum(self.slots)

#En este ejemplo, la clase MiArray tiene tres métodos principales:

#El método __init__ se utiliza para inicializar la instancia de la clase y toma un parámetro 
# size, que representa el tamaño del array.

#El método poblar_aleatorio se encarga de poblar los slots del array con números aleatorios. 
# Toma un parámetro limite, que establece el rango máximo de los números aleatorios generados.

#El método poblar_secuencial se utiliza para poblar los slots del array con números secuenciales, 
# desde 1 hasta el tamaño del array.

# El método sumar_valores calcula la suma de todos los valores presentes en el array y devuelve 
# el resultado.

# Aquí hay un ejemplo de cómo utilizar la clase MiArray:

# Crear una instancia de la clase MiArray
mi_array = MiArray(5)

# Poblar los slots del array con números aleatorios
mi_array.poblar_aleatorio(100)

# Imprimir el array
print(mi_array.slots)

# Sumar los valores del array
suma = mi_array.sumar_valores()
print("Suma:", suma)

