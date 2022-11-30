import random

game = ["Rock", "Paper", "Scissors"]

user_choice = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
computer_choice = random.randint(0, 2)
if (user_choice < 0) or (user_choice > 2):
    print("Invalid Values, You lose!")
else:
    print(f"You chose {game[user_choice]}")
    if user_choice == 0:
        if computer_choice == 0:
            print(f"Computer chose {game[computer_choice]}\nDRAW!")
        elif computer_choice == 1:
            print(f"Computer chose {game[computer_choice]}\nCOMPUTER WON!")
        else:
            print(f"Computer chose {game[computer_choice]}\nYOU WON!")
    elif user_choice == 1:
        if computer_choice == 0:
            print(f"Computer chose {game[computer_choice]}\nYOU WON!")
        elif computer_choice == 1:
            print(f"Computer chose {game[computer_choice]}\nDRAW!")
        else:
            print(f"Computer chose {game[computer_choice]}\nCOMPUTER WON!")
    else: 
        if computer_choice == 0:
            print(f"Computer chose {game[computer_choice]}\nCOMPUTER WON!")
        elif computer_choice == 1:
            print(f"Computer chose {game[computer_choice]}\nYOU WON!")
        else:
            print(f"Computer chose {game[computer_choice]}\nDRAW!")