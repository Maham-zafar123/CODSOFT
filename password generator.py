import random
import string

alphabet = string.ascii_letters
digits = string.digits
low_characters = "@#$%"
characters = "~!@#]<>+=-/$%^[&*()_}|:;{.,/"
total = ""


def generatePassword(level, length):
    if level == "simple":
        total = alphabet + digits
        password = "".join(random.choice(total) for x in range(length))
        return password
    elif level == "medium":
        total = alphabet + digits + low_characters
        password = "".join(random.choice(total) for x in range(length))
        return password
    elif level == "tough":
        total = alphabet + digits + characters
        password = "".join(random.choice(total) for x in range(length))
        return password
    else:
        return "Invalid choice. Please Enter ['simple,'medium,'tough']"


def welcome_msg():
    print("\t\t\n☆*: .｡. o(≧▽≦)o .｡.:*☆ Welcome To MY PASSWORD GENERATOR ☆*: .｡. o(≧▽≦)o .｡.:*☆")


def display_menu():
    print("\n\t\t\t@@@@@[HERE IS THE MAIN MENU:]@@@@@\n")
    print("\t\t → Press 1 to Generate a password")
    print("\t\t → Press 2 to check the rules for the Generation of a password")
    print("\t\t → Press 3 to exit")


def RULES():
    print("\t\t → When you Choice 'Simple' Password only include letters and numbers.")
    print("\t\t → When you Choice 'Medium' Password only include letters,Numbers and some low characters. ")
    print("\t\t → When You Choice 'Tough' Password include letters,Numbers And Special Character.")


try:
    while True:
        welcome_msg()
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(
                input("Enter desired length of Password (min=4, max=16): "))
            while length not in range(4, 21):
                print("Length not Suitable")
                length = int(input("Enter Length Again: "))

            list2 = ['simple', 'medium', 'tough']
            level = input(
                "Enter Complexity level ('simple', 'Medium', 'tough'): ").lower()
            while level not in list2:
                print("Invalid Input")
                level = input(
                    "Enter Complexity level ('simple', 'Medium', 'tough'): ").lower()

            password = generatePassword(level, length)
            print(f"\n\t\tPassword Generated is: {password}")

        elif choice == "2":
            RULES()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

except KeyboardInterrupt:
    print("\nKeyboardInterrupt. Exiting...")
except Exception as e:
    print(f"An error occurred: {str(e)}. Exiting...")
