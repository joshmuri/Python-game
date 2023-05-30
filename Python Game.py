# import random library
import random

# Print the welcome message to user
print("Welcome to the Rock Paper Scissors Game.")

# Game rules
print("Game rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")

# Define suitable variables
user_choices = ['Rock','Paper','Scissors']
player_choice = ""

# Scores
your_score = 0
computer_score = 0

# Print a start game message
print("Start the game")

# create a loop
while True:
    player_choice = input("Make a choice : ")

    if player_choice not in user_choices:
        print("Hey that's not allowed!")
        continue

    # Computer chooses the 'user_choices' at random
    computer_choice = random.choice(user_choices)
    print("Computer plays", computer_choice)

    # check for conditions
    if player_choice == computer_choice:
        print("It's a tie")
    elif player_choice == 'Rock' and computer_choice == 'Scissors':
        print("You win!")
        your_score = your_score + 1
    elif player_choice == 'Paper' and computer_choice == 'Rock':
        print('You win')
        your_score = your_score + 1
    elif player_choice == 'Scissors' and computer_choice == 'Paper':
        print('You win')
        your_score = your_score + 1
    else:
        print('You lost')
        computer_score = computer_score + 1

    print("You :",your_score,"   ", computer_score,": Computer")

    # prompt the user to play again or quit
    new_game = input('Play again?(Y/N) :')

    if new_game == 'N':
        break