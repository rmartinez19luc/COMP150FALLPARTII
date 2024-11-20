from cyborg_boss import cyborg_boss_battle

def futuristic_portal():
    print("You have entered the Futuristic Portal.")
    print("You are now in a futuristic world.")
    print("You have the option to fight the Cyborg Boss or run away.")
    print("What would you like to do?")
    print("1. Fight the Cyborg Boss")
    print("2. Run away")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You have chosen to fight the Cyborg Boss.")
        print("Prepare for battle!")
        cyborg_boss_battle()  # Call the battle logic from cyborg_boss.py
    elif choice == "2":
        print("You have chosen to run away.")
        print("You have successfully escaped the Futuristic Portal.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
