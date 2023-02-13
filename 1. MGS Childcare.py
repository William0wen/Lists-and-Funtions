children = []
choice = 0


# Drop off function
def dropOff():
    name = input("Enter the child's name: ").lower()
    children.append(name)


# Pick up function
def pickUp():
    pickup = input("Enter the name of the child you want to pick up: ").lower()
    if pickup not in children:
        print("Error: Invalid child name")
    else:
        children.remove(pickup)


# Calculate cost function
def calcCost():
    hours = int(input(f"How many hours are your {len(children)} children going to stay? "))
    print(f"Total cost is ${len(children * 12 * hours)}")


# Print roll function
def printRoll():
    for child in children:
        print(f"{child}")


# Main

while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------\n")
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system\n")
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        dropOff()

    elif choice == 2:
        pickUp()

    elif choice == 3:
        calcCost()

    elif choice == 4:
        printRoll()

    else:
        exit("Goodbye")
