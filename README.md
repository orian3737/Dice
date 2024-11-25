# D&D Dice Roller

A simple command-line program to roll various dice used in Dungeons & Dragons and other tabletop RPGs. This tool allows users to select a die, roll it multiple times, and return to the die selection menu as needed. It also provides special feedback for critical rolls on a D20 die.

## Features

- Choose from commonly used dice: D4, D6, D8, D10, D12, and D20.
- Roll the selected die as many times as you want.
- Special messages for D20 rolls:
  - Rolling a `1`: Displays **"Critical Failure!"**
  - Rolling a `20`: Displays **"Critical Hit!!!"**
- Return to the die selection menu by typing `R`.
- Exit the program anytime by selecting option `7` from the main menu.

## How to Use

1. Run the program in your terminal:

   ```bash
   python dnd_dice_roller.py

Follow the on-screen instructions:

Select a die: Choose from the dice menu by entering a number (e.g., 1 for D4, 2 for D6, etc.).
Roll the die: Press Enter to roll the die and see the result.
Return to the menu: Type R to return to the main die selection menu.
Exit the program: Select 7 from the main menu or press Ctrl+C to quit.
Example Interaction
plaintext
Copy code
Welcome to the D&D Dice Roller!

Choose a die to roll:

1. D4 (4 sides)
2. D6 (6 sides)
3. D8 (8 sides)
4. D10 (10 sides)
5. D12 (12 sides)
6. D20 (20 sides)
7. Exit the program
Enter your choice (1-7): 6

Rolling a D20 die. Type 'R' to return to the die menu:
Press Enter to Roll or 'R' to Exit:
You Rolled: 15
Press Enter to Roll or 'R' to Exit:
You Rolled: A CRITICAL FAILURE!
Press Enter to Roll or 'R' to Exit:
You Rolled: A CRITICAL HIT!!!
Press Enter to Roll or 'R' to Exit: R

Choose a die to roll:

1. D4 (4 sides)
2. D6 (6 sides)
3. D8 (8 sides)
4. D10 (10 sides)
5. D12 (12 sides)
6. D20 (20 sides)
7. Exit the program
Enter your choice (1-7): 7
Thanks for playing! Goodbye.
Requirements
Python 3.6 or higher
random module (part of Python's standard library)
File Structure
plaintext
Copy code
.
├── dnd_dice_roller.py   # Main Python program file
├── README.md            # This documentation file
Code Explanation
Main Functions
roll_die(sides: int) -> int
Rolls a die with the specified number of sides and returns the result.

die_selection_menu()
Displays a menu of available dice and allows the user to select one. Includes an option to exit the program.

roll_menu(sides: int)
Allows the user to roll the selected die repeatedly. Special messages are displayed for critical rolls (1 or 20) on a D20 die. The user can return to the main menu by typing R.

main()
Runs the main program loop, managing the die selection menu and roll menu.

Future Enhancements
Add support for custom dice (e.g., D100).
Include functionality to roll multiple dice simultaneously.
Add a GUI version for a more interactive experience.
Contributing
Feel free to submit issues or pull requests if you have ideas for improvements or bug fixes.

License
This project is licensed under the MIT License. You are free to use, modify, and distribute this program as you like.

Enjoy rolling your dice, and may your rolls always be critical hits!