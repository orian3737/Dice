import random


def roll_die(sides: int) -> int:
    """Roll a die with the given number of sides."""
    return random.randint(1, sides)
    
    
def die_selection_menu():
    """Display the die selection menu and return the selected die."""
    print("\nChoose a die to roll:")
    print("1. D4 (4sides)")
    print("2  D6 (4 sides)")
    print("3. D8 (8 sides)")
    print("4. D10 (10sides)")
    print("5. D12 (12 sides)")
    print("6. D20 (20 sides)")
    print("7. Exit the program")
    while True:
        try:
            choice = input("Enter your choice (1-7):").strip()
            if choice == '7':
                print("Thanks for playing! GoodBye.")
                exit()
            elif choice in {'1','2','3','4','5','6'}:
                sides = [4, 6, 8, 10, 12, 20][int(choice) - 1]
                return sides
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def roll_menu(sides: int):
    """Allow the user to roll the selected die untill they choose to return."""
    print(f"\nRolling a D{sides} die. Type 'R' to return to Die menu:")
    while True:
        command = input("Press Enter to Roll or 'R' to Exit: ").strip().upper()
        if command == 'R':
            break
        roll = roll_die(sides)
        if sides == 20:
            if roll == 1:
                print("You rolled a 'CRITICAL FAILURE!'")
            elif roll == 20:
                print("You rolled a 'CRITICAL HIT!!!'")
            else:
                print(f"You Rolled: {roll}")
        else:
            print(f"You Rolled: {roll}")
    
def main():
    """Main program loop"""
    print("Welcome to the D&D Dice Roller!")
    while True:
        sides = die_selection_menu()
        roll_menu(sides)
            
if __name__ == "__main__":
    main()
        
