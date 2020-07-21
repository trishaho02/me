"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    guessesTaken = 0

    print("\nWelcome to the guessing game!")
    print("Enter a number between _ and _")

    while True:
      lowerBound = input("Enter a lower bound: ")
      if type(lowerBound) != int:
        print("Please enter an integer")
      else:
        break 
    
    while True:
      upperBound = input("Enter a upper bound: ")
      if type(upperBound) != int:
        print("Please enter an integer")
      else:
        break

    print("Ok then, a number between {}".format(lowerBound))
    lowerBound = int(lowerBound)
    print("and {}".format(upperBound))

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed: 
      try:
        guessedNumber = int(input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),)
        
        if guessedNumber == actualNumber:
          print("It was {}".format(actualNumber))
          guessed = True 
        if guessedNumber < actualNumber:
          print("Too small, try again :'(")
        if guessedNumber > actualNumber:
          print("Too big, try again :'(")
        if guessedNumber > upperBound or guessedNumber < lowerBound:
          print("Your number is outside the given range.")
      except:
        print("Please enter an integer")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
