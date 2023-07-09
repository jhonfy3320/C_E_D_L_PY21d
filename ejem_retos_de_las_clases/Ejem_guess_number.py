'''
En este juego, el programa genera un número aleatorio entre 1 y 100 usando la random.randint()función. 
Luego se le pide al usuario que adivine el número, y el programa proporciona comentarios 
("¡Demasiado bajo!" o "¡Demasiado alto!") en función de si la suposición es más baja o más alta que el 
número objetivo. Si el usuario adivina correctamente el número, el programa muestra un 
mensaje de felicitación junto con la cantidad de intentos que tomó.'''

import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Initialize the guess count
guesses_taken = 0

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    # Get user's guess
    guess = int(input("Take a guess: "))
    guesses_taken += 1
    
    # Compare the guess with the target number
    if guess < number:
        print("Too low! Try a higher number.")
    elif guess > number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You guessed the number in {guesses_taken} attempts!")
        break
