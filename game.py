import random

def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious forest. What do you do?")
    print("1. Explore")
    print("2. Rest")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        explore()
    elif choice == "2":
        rest()
    elif choice == "3":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Please select a valid option.")
        start_game()

def explore():
    print("You venture deeper into the forest and discover a hidden cave.")
    print("Do you want to enter the cave?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")

    if choice == "1":
        enter_cave()
    elif choice == "2":
        print("You decide not to enter the cave.")
        start_game()
    else:
        print("Invalid choice. Please select a valid option.")
        explore()

def enter_cave():
    print("Inside the cave, you find a treasure chest.")
    print("Do you want to open it?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")

    if choice == "1":
        open_chest()
    elif choice == "2":
        print("You leave the treasure chest untouched.")
        start_game()
    else:
        print("Invalid choice. Please select a valid option.")
        enter_cave()

def open_chest():
    treasure = random.choice(["gold coins", "magical gem", "old map"])
    print(f"You open the treasure chest and find {treasure}!")
    print("Congratulations! You've won the game.")

def rest():
    print("You decide to take a rest and regain your energy.")
    print("You feel refreshed and ready for your next adventure.")
    start_game()

start_game()
