import random

name = input("What's your name? : ")
options = ["rock", "paper", "scissors"]
computer_score = 0
user_score = 0

print("Let's start the game of rock, paper, scissors!")
user_guess = input("You are playing first to 5 points with the computer, make your guess: ")

while user_score < 5 and computer_score < 5:
    computer_guess = random.choice(options)
    print("Computer guess:", computer_guess)

    if user_guess == "rock":
        if computer_guess == "paper":
            computer_score += 1
        elif computer_guess == "scissors":
            user_score += 1
    elif user_guess == "paper":
        if computer_guess == "scissors":
            computer_score += 1
        elif computer_guess == "rock":
            user_score += 1
    elif user_guess == "scissors":
        if computer_guess == "rock":
            computer_score += 1
        elif computer_guess == "paper":
            user_score += 1

    print("Computer =", computer_score, "-", name, "=", user_score)
    if user_score < 5 and computer_score < 5:
        user_guess = input("Guess again: ")

if user_score == 5:
    print(f"Congratulations {name}, you won!")
else:
    print("Sorry, the computer won. Better luck next time!")
