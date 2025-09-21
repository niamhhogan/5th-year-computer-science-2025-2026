"""
---------------------------------------------------------------
5th Year Computer Science – Class 1: Introduction to Python
---------------------------------------------------------------

Leaving Certificate Learning Outcomes

---------------- Strand 1: Practices and Principles ----------------
S1: Computational Thinking
  - 1.1 Describe a systematic process for solving problems and making decisions
      * Following structured steps: print statements, variables, blank lines
  - 1.3 Solve problems by deconstructing them into smaller units
      * Mini Challenge Project: breaking program into variables, then print blocks
  - 1.4 Solve problems using logic
      * Debugging tasks (Task 6) and ordering program steps logically

S1: Designing and Developing
  - 1.22 Read, write, test, and modify computer programs
      * All exercises, Mini Challenge Project
  - 1.23 Reflect and communicate on design and development process
      * Using comments to explain code and program logic

---------------- Strand 2: Core Concepts ----------------
S2: Abstraction
  - 2.1 Use abstraction to describe systems and relationship between wholes and parts
      * Variables and print statements as parts and whole of program
  - 2.3 Implement modular design
      * Writing small independent code blocks before combining them in Mini Challenge Project

S2: Algorithms
  - 2.6 Construct algorithms using sequences, selections, loops, operators
      * Sequential steps in “About Me” program
  - 2.7 Implement algorithms using a programming language
      * Translating planned steps into Python code

S2: Data
  - 2.16 Use data types common to procedural high-level languages
      * Strings and integers used in variables

S2: Evaluation and Testing
  - 2.20 Identify and fix/debug warnings and errors in code
      * Tasks on syntax errors and debugging
  - 2.21 Reflect on limitations of completed code
      * Using comments and reviewing Mini Challenge Project output




Python Version:
The latest version of Python is 3.12. Check which version you are using in the Shell

Today we are starting to learn Python! 

Python is:
- A high-level, interpreted programming language.
- Known for its readability and simplicity.
- Used for web development, data analysis, AI, automation, games, and more.
- Great for beginners but also powerful for advanced projects.

IDEs (Integrated Development Environments):
We will be using Thonny and Visual Studio Code (VS Code) to write and run Python programs.
- An IDE helps you write, run, and debug code.
- Key parts of the IDE:
  1. Editor
     - This is where you write your Python code.
  2. Shell / Console
     - Shows the output of your program and any error messages.
     - You can also type Python commands here to test small pieces of code.
- Thonny is very beginner-friendly and ideal for learning.
- VS Code is more powerful and widely used in industry.
"""

"""
---------------------------------------------------------------
Printing to the Screen
---------------------------------------------------------------
- Python uses the print() function to display output on the screen.
- You can print text, numbers, variables, or a combination.
"""

# Examples:
print("Hello, world!")                 # Prints text
print(5 + 3)                           # Prints the result of a calculation
print("I am", 16, "years old")         # Prints multiple items separated by spaces

# Printing Blank Spaces:
print()                                # Prints a blank line
print("Line 1\nLine 2")                # Moves to a new line
print("Line 1\n\nLine 3")              # Adds an extra blank line

# Escape Characters:
print("Hello, \nMy name is Niamh\n\tThis is how to tab in")
print("This is a backslash: \\")

# Common Errors in print statements (do NOT run):
# print(hello)        # Error: hello is not defined as a variable or string
# Print("Hello")      # Error: Python is case-sensitive (print must be lowercase)
# print("Hello)       # Error: Missing closing quote

# Task 1:
# - Print your name
# - Then print two blank lines
# - Then print your age

# Task 2 (optional challenge):
# - Print a short message using \n and \t to format it nicely
# - Include at least one backslash (\\) in your output
"""

---------------------------------------------------------------
Data Types
---------------------------------------------------------------
Python has several basic data types:

1. Strings (str)         # Text inside quotes: "Hello" or 'Python'
2. Integers (int)        # Whole numbers: 5, 100, -3
3. Floating-point (float) # Numbers with decimals: 3.14, -0.5
4. Boolean (bool)        # True or False

# Examples:
name = "Tom"       
age = 16           
height = 1.65      
student = True     

# Task 3:
# - Create three variables using different data types (str, int, float)
# - Assign values to them (you can use your own name, age, height)
# - Print the values
"""

"""
---------------------------------------------------------------
Variable Naming Conventions
---------------------------------------------------------------
- Variables store data and should have meaningful names.
- Rules:
  * Can contain letters, numbers, and underscores (_)
  * Must start with a letter or underscore
  * Cannot use spaces or special characters
  * Case-sensitive (age and Age are different)
- Recommended style: lowercase with underscores for readability

# Good examples:
favourite_food = "Pizza"
my_age = 16
height_in_m = 1.65

# Bad examples:
# 2ndName = "Tom"       # starts with a number (invalid)
# my-age = 16           # contains hyphen (invalid)
# print = "Hello"       # uses a Python keyword (not recommended)

# Task 4:
# - Create three variables following the naming conventions
# - Assign values and print them
# - Use meaningful names and correct formatting
"""

"""
---------------------------------------------------------------
Strings
---------------------------------------------------------------
- Strings are text inside quotes (single ' ' or double " ")
- You can combine strings with variables in several ways
"""

# Examples of strings
print("Hello")                 
print('Python is fun!')        

# Combining strings and variables
favourite_food = "Pizza"
age = 16

# Using comma to combine
print("My favourite food is", favourite_food)

# Using concatenation with +
print("I am " + str(age) + " years old.")  

# Using f-strings (Python 3.6+)
print(f"My favourite food is {favourite_food} and I am {age} years old.")

# Task 5:
# - Create a variable called favourite_food
# - Assign your favourite food as a string
# - Print a message: "My favourite food is <favourite_food>"

# Task 6 (optional challenge):
# - Create a variable for your favourite hobby
# - Print a sentence combining your name, age, favourite food, and hobby using:
#   1. Commas
#   2. Concatenation (+)
#   3. f-strings
"""

"""
---------------------------------------------------------------
Comments in Python
---------------------------------------------------------------
# Single-line comments start with #
''' Multi-line comments use triple quotes '''
"""

# Example single-line comment
print("Hello")  # Comment explaining this print statement

# Example multi-line comment
"""
This is a multi-line comment.
It can span several lines.
Useful for longer explanations or notes.
"""

# Task 7:
# - Add single-line and multi-line comments to explain your favourite_food code
"""

"""
---------------------------------------------------------------
Syntax Errors and Bugs
---------------------------------------------------------------
- Syntax errors happen when Python cannot understand your code
- Bugs are mistakes that make code behave differently than expected
"""

# Examples of syntax errors (do not run):
# print("Hello)  # Missing closing quote
# prin("Hello") # Misspelled print

x = 10
y = 5
print(x - y)  # If we wanted addition, using - is a bug

# Task 8:
# - Look at the following code and fix the errors:
# print("Python is fun!)
# number = 5
# number = number + "2"  # Bug: adding string to integer
"""

"""
---------------------------------------------------------------
Mini Challenge Project
---------------------------------------------------------------
Goal: Create a simple “About Me” program that uses variables, strings, print statements,
blank lines, and comments.
"""

# Example solution structure (students can modify):

# Variables
my_name = "Tom"
my_age = 16
favourite_food = "Pizza"
favourite_colour = "Blue"
favourite_hobby = "Reading"

# Print statements with blank lines
print("About Me")
print()  # Blank line
print("Name:", my_name)
print("Age:", my_age)
print()  # Blank line
print("Favourite Food:", favourite_food)
print("Favourite Colour:", favourite_colour)
print("Favourite Hobby:", favourite_hobby)

# Task 9:
# - Create your own version of this “About Me” program.
# - Try adding at least one extra line of information about yourself.
# - Use comments to explain each variable and print statement.
"""

"""
---------------------------------------------------------------
Recap
---------------------------------------------------------------
- Python is simple, readable, and widely used.
- IDEs like Thonny and VS Code help us write and run Python code.
- Today we learned:
  * How to print output and blank lines
  * What variables and strings are
  * Single-line and multi-line comments
  * Recognising syntax errors and bugs
- Practice these concepts before the next class!
"""
