import os
from datetime import datetime

# Dictionary to store task lists
User_Task = {}


def welcommsg(name):
    print(
        f"\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ Welcome {name} To My TO DO LIST APPLICATION ☆*: .｡. o(≧▽≦)o .｡.:*☆ ")
    print("→ Press 1 to Update list: \n→ Press 2 to track list: \n→ Press 3 to exit: \n")


def update_list(name):
    print(f"Welcome, {name}, to EDIT Menu")
    namelist = input(
        "Enter the name of the list in which you want to add tasks: \n")

    # Check if the list already exists, if not, create it
    if namelist not in User_Task:
        User_Task[namelist] = []

    def add_task(Name):
        timestamp = datetime.now()  # Get the current date and time
        User_Task[namelist].append(
            {"Name": Name, "Completed": False, "Timestamp": timestamp})

    def list_task():
        for x, task in enumerate(User_Task[namelist], start=1):
            status = "Done" if task["Completed"] else "Not Done"
            timestamp = task["Timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{x}. {task['Name']} - {status} (Added on: {timestamp})")

    def Completed(Task_number):
        User_Task[namelist][Task_number - 1]["Completed"] = True
        User_Task[namelist][Task_number - 1]["Timestamp"] = datetime.now()

    def Remove_task(Task_number):
        del User_Task[namelist][Task_number - 1]

    while True:
        choice = int(input(
            "  →Press 1 to Add task: \n  →Press 2 to Lists the Tasks: \n  →Press 3 to Mark a Complete a task: \n  →Press 4 to Delete The task: \n  →Press 5 to Return to Main menu: \n  →Press 6 to exit the program : \n"))
        if choice == 1:
            Taskname = input("Enter task Name: ")
            add_task(Taskname)
        elif choice == 2:
            list_task()
        elif choice == 3:
            Mark = int(input("Enter task number to mark as completed: "))
            Completed(Mark)
        elif choice == 4:
            delete = int(input("Enter the number of the task to delete it: "))
            Remove_task(delete)
        elif choice == 5:
            break
        elif choice == 6:
            exit(0)
        else:
            print("Invalid Choice!")


def track_task():
    print(f"Welcome, {name}, to Tracking List ")
    Taskname = input("Enter the name of the task list you want to track: ")
    if Taskname in User_Task:
        for task in User_Task[Taskname]:
            status = "Done" if task["Completed"] else "Not Done"
            timestamp = task["Timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{task['Name']} - {status} (Added on: {timestamp})")
    else:
        print(f"List with the name '{Taskname}' does not exist.")


name = input("Please Enter Your Name: ")

while True:
    welcommsg(name)
    choice = int(input("Enter Choice: "))
    if choice == 1:
        update_list(name)
    elif choice == 2:
        track_task()
    elif choice == 3:
        exit(0)
    else:
        print("Invalid Choice")
