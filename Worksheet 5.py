#Number guessing game
"""
import math
import random

lower = int(input("Enter a number :"))
upper = int(input("Enter a number :"))
randomChoice = random.randint(lower, upper)
minNumberGuesses = round(math.log(upper - lower + 1, 2))

x = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
count = 0
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    guess = int(input("Guess a number: "))
 
    if x == guess:
        print("Congratulations you guessed right! You done it in ",
              count, " try(s)")
        break
    elif x > guess:
        print("Higher")
    elif x < guess:
        print("Lower")
    
if count >= math.log(upper - lower + 1, 2):
    print("The number was", x)
"""
#Number guessing game /|\
 
