import random


def welcome_msg():
    print("\n\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ Welcome To MY ROCK, PAPER, SCISSORS GAME ☆*: .｡. o(≧▽≦)o .｡.:*☆")
    print("\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ Please Enter Your Choice To Play the game ☆*: .｡. o(≧▽≦)o .｡.:*☆")


def winnermsg():
    print("\n\t\tHurrah!.....You have won this game !!!!!!!!😍😍😍😍😍\n")


def losermsgs():
    print("\n\t\tOOPS!...... you lost this game!!!!!!😢😢😢😢 \n")


def turns_both(computer_choice, user_choice):
    print(f"\n\t\t→ Computer's Turn is {computer_choice}.\n")
    print(f"\n\t\t→ User's Turn is {user_choice}.\n")


def winner_announcment(winning_choice, losing_choice):
    print(
        f"\n\t\t{winning_choice.capitalize()} beats the {losing_choice.capitalize()}\n")


list_choice = ["rock", "scissor", "paper"]
RULES_game = "\n\t\t  → Rock wins against Scissor\n\t\t  → Paper wins against Rock\n \t\t  → Scissor wins against Paper\n"


def gamewin(computer_choice, user_choice):
    if not (user_choice in ['rock', 'scissor', 'paper']):
        print("Invalid Input!!!..choose any ['rock','scissor','paper']")
        return

    if computer_choice == user_choice:
        print("\n\t\tOHHHH Game is TIE!!!\n")
    elif computer_choice == 'rock':
        if user_choice == 'paper':
            winnermsg()
            winner_announcment(user_choice, computer_choice)
        else:
            losermsgs()
            winner_announcment(computer_choice, user_choice)
    elif computer_choice == 'scissor':
        if user_choice == 'rock':
            winnermsg()
            winner_announcment(user_choice, computer_choice)
        else:
            losermsgs()
            winner_announcment(computer_choice, user_choice)
    elif computer_choice == 'paper':
        if user_choice == 'scissor':
            winnermsg()
            winner_announcment(user_choice, computer_choice)
        else:
            losermsgs()
            winner_announcment(computer_choice, user_choice)


welcome_msg()

while True:
    choice = int(input(
        "Enter a number:   \n\n\t\t  → Press 1 to see the RULES of the game : \n\t\t  → Press 2 to continue the game : \n\t\t  → Press 3 to exit : "))
    if choice == 1:
        print(RULES_game)
    elif choice == 2:
        computer_choice = random.choice(list_choice)
        user_choice = input(
            "Enter Your Choice ('rock','scissor','paper'):    \n→  ").lower()
        turns_both(computer_choice, user_choice)
        gamewin(computer_choice, user_choice)
    elif choice == 3:
        exit()
    else:
        print("Invalid Choice!")
