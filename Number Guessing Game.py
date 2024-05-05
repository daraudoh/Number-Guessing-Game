from random import seed
from random import randint

number = randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
  guess = int(input("Make a guess: "))
  if guess == number: 
      print("You guessed the right number!") 
      break # This will break the loop if the user guesses the right number.

  elif guess > number: # This will check if the user's guess is higher than the number.
        print("Too high.") 
        
  elif guess < number: # This will check if the user's guess is lower than the number.
        print("Too low.")
        

    