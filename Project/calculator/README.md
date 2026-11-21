Python Command-Line Calculator

Welcome to my first Python project! This is a simple command-line calculator program built in Python that evaluates mathematical expressions while following basic operator precedence (BODMAS/PEMDAS).

🚀 Features

Basic Arithmetic Operations:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Operator Precedence (Order of Operations):

Evaluates multiplication (*) and division (/) first.

Evaluates addition (+) and subtraction (-) second.

Zero Division Guard: Includes safety checks to prevent crashes when dividing by zero.

🛠️ How It Works

User Input: The program prompts you to enter a mathematical string (e.g., 10 + 5 * 2).

Formatting & Tokenization: Spaces are automatically added around math operators to ensure clean string splitting into individual tokens (numbers and operators).

First Pass (Multiplication & Division): The code scans the token array from left to right, performing * and / operations first and updating the expression list in place.

Second Pass (Addition & Subtraction): The remaining expression list is scanned again from left to right to calculate + and - operations.

Output: The final evaluated result is printed to the console.

📋 Prerequisites

Python 3.x installed on your system.

📦 How to Run

Clone or download this repository.

Open your terminal or command prompt and navigate to the project directory.

Run the Python script:

python calculator.py


Enter an equation when prompted:

enter the values you want to calculate: 12 + 4 * 2
the equation is being solved please wait a while 12 + 4 * 2
result: 20.0


🌟 Future Improvements

Here are a few features planned for future versions of this project:

Support for parentheses () to customize order of operations.

Support for negative numbers at the beginning of an equation or after an operator.

A continuous while loop to allow multiple calculations without re-running the script each time.

Improved error handling for invalid user inputs (e.g., entering letters instead of numbers).

👤 Author

Created as a first Python project to learn functions, loops, and basic parsing techniques.
