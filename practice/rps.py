# TODO: Develop a console-based Rock Paper Scissors game in Python
# Game should be modular, allowing for easy updates or rule changes
# Include user input for selecting options and display game results

import random

def rps():
    print("Welcome to Rock Paper Scissors!")
    print("Enter 'q' to quit")
    print("Enter 'r' for Rock")
    print("Enter 'p' for Paper")
    print("Enter 's' for Scissors")
    print("")

    while True:
        user = input("Enter your choice: ")
        computer = random.choice(['r', 'p', 's'])

        if user == 'q':
            break

        if user == computer:
            print("It's a tie!")
            continue

        if is_win(user, computer):
            print("You won!")
        else:
            print("You lost!")

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

rps()
