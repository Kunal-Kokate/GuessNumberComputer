import random

def computer_guess():
    low = int(input("Inputting the range. Enter a low number: "))
    high = int(input("Inputting the range. Enter a high number: "))

    while low > high:
        print("The first number must be lower than the second number")
        low = int(input("Inputting the range. Enter a low number: "))
        high = int(input("Inputting the range. Enter a high number: "))

    feedback = ''

    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (h), too low (l), or correct(c): ")

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"You are correct the number was {guess}")

computer_guess()