from array import Array 


class grid():
    def __init__(self, rows, column, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(column, fill_value)

    def get_height(self):
        return len(self.data)

# metodod para optener su ancho  
   
    def get_widht(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
# Hacer la reprecentacion en strin de algunos de esos nombres 

    def __str__(self) -> str:
        result = ''

        for row in range(self.get_height()):
            for col in range(self.get_widht()):
                result += str(self.data[row][col]) + " "

            result += '\n'

        return str(result)
    
