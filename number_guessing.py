import random
number = random.randint(1,9)
chances = 0
while chances < 5 :
    guess = int(input("Enter your guess: "))
    if guess == number :
        print("Congratulations YOU WON !!")
        break
    elif guess > number :
        print("Guess is too high. Try something lower than",guess)
        chances=chances+1
    else :
        print("Guess is too low. Try something higher than",guess)
        chances=chances+1
if not chances < 5 :
    print("YOU LOSE !! The number is",number)