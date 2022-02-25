import random

print("********************************")
print("Welcome to the guessing game!")
print("********************************")

user_number = input("Guess a number among 0 and 10\n")

random_number = random.randint(0,10)

if (user_number == random_number):

    print(f"You guessed {user_number} congratulations you guessed it right the random number is {random_number}")

else:

    print(f"You guessed {user_number} sorry you guessed it wrong the random number is {random_number}")

    print("End of the game")
