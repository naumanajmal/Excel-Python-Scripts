import random


def guess(x):
    guessn = 0
    number = random.randint(1, x)
    while guessn != number:
        guessn = int(input("Enter Number "))
        difference = abs(number - guessn)
        if (guessn < number) and (difference > 10):
            print("Number is too low guess again:")
        elif (guessn > number) and (difference > 10):
            print("Number is too high guess again:")
        elif (guessn < number) and (difference < 10):
            print("Number is low guess again, you are very close try again:")
        elif (guessn > number) and (difference < 10):
            print("Number is high guess again, you are very close try again:")
    print(f"you guess the number{guessn}")
guess(15)


