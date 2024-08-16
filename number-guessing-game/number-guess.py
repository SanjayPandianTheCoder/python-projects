import math
import random

upperBound = int(input("Enter upper bound : "))
lowerBound = int(input("Enter lower bound : "))

if upperBound < lowerBound:
    print("Upper bound should be greater than lower bound")
    exit(0)

guess = random.randint(lowerBound, upperBound)
chances = math.ceil(math.log((upperBound - lowerBound + 1), 2))
count = 0

print("You have only {0} chances".format(chances))

while count < chances:
    count += 1

    currentGuess = int(input("Enter a guess : "))
    if currentGuess == guess:
        print("CONGRATS! You have found the number with {0} guesses left".format(chances - count))
        exit(0)

    else:
        if currentGuess < guess:
            print("your guess is low")
        else:
            print("your guess is high")
    
    print("You have {0} chances left".format(chances-count))

print("The number is ",guess)
    

    