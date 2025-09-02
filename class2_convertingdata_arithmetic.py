"""
---------------------------------------------------------------
5th Year Computer Science – Class 2: Data Types & Arithmetic
---------------------------------------------------------------

Leaving Certificate Learning Outcomes

---------------- Strand 1: Practices and Principles ----------------
S1: Computational Thinking
  - 1.1 Describe a systematic process for solving problems and making decisions
      * Revision tasks and applying structured steps to new problems
  - 1.3 Solve problems by deconstructing them into smaller units
      * Breaking calculations into input, processing, and output
  - 1.4 Solve problems using logic
      * Applying order of operations and debugging incorrect calculations

S1: Designing and Developing
  - 1.22 Read, write, test, and modify computer programs
      * All exercises and combination tasks
  - 1.23 Reflect and communicate on design and development process
      * Using comments to explain reasoning and outputs

---------------- Strand 2: Core Concepts ----------------
S2: Abstraction
  - 2.1 Use abstraction to describe systems and relationship between wholes and parts
      * Separating input, calculation, and output in programs

S2: Algorithms
  - 2.6 Construct algorithms using sequences, selections, loops, operators
      * Using sequential steps for arithmetic operations
  - 2.7 Implement algorithms using a programming language
      * Writing Python code for calculations and conversions

S2: Data
  - 2.16 Use data types common to procedural high-level languages
      * Conversion between strings, integers, floats, and rounding

S2: Evaluation and Testing
  - 2.20 Identify and fix/debug warnings and errors in code
      * Common type conversion and arithmetic errors
  - 2.21 Reflect on limitations of completed code
      * Reviewing precision and rounding issues in calculations
"""

"""
---------------------------------------------------------------
Revision / Recap of Class 1
---------------------------------------------------------------
- Last class we learned about: print statements, variables, strings, comments, and bugs.
"""

# Task 1: Revision
# 1. Create variables for your name, age, and favourite colour
# 2. Print them neatly with labels (e.g., "Name:", "Age:")
# 3. Add comments to explain each variable
# 4. Intentionally make one error (e.g., missing quote) and fix it

"""
---------------------------------------------------------------
Converting Between Data Types
---------------------------------------------------------------
- Sometimes we need to change one data type into another.
- Common functions:
  * int() → convert to integer
  * float() → convert to floating point
  * str() → convert to string
"""

# Examples:
x = "5"
print(int(x) + 10)   # Converts string to integer before adding
y = 3.7
print(int(y))        # Converts float to integer (truncates, does not round)
print(str(20))       # Converts integer to string

# Task 2:
# - Create a string variable with the value "25"
# - Convert it to an integer and add 5
# - Create a float variable and convert it to a string to print in a sentence

"""
---------------------------------------------------------------
Arithmetic Operations
---------------------------------------------------------------
Python supports all standard arithmetic operations:

+   Addition
-   Subtraction
*   Multiplication
/   Division (always returns float)
//  Floor Division (drops remainder)
%   Modulus (gives remainder)
**  Exponent (powers)
"""

# Examples:
print(5 + 2)     # 7
print(5 - 2)     # 3
print(5 * 2)     # 10
print(5 / 2)     # 2.5
print(5 // 2)    # 2
print(5 % 2)     # 1
print(2 ** 3)    # 8

# Task 3:
# - Use each operator at least once with numbers of your choice
# - Print the results with labels (e.g., "Addition:", result)

"""
---------------------------------------------------------------
Incrementing
---------------------------------------------------------------
- Incrementing means increasing the value of a variable.
- Decrementing means decreasing it.
"""

# Examples:
x = 10
x += 1   # increment by 1
print("After increment:", x)

x -= 2   # decrement by 2
print("After decrement:", x)

# Task 4:
# - Create a variable starting at 100
# - Increment it by 5 three times (x += 5)
# - Decrement it by 10 once (x -= 10)
# - Print the final value

"""
---------------------------------------------------------------
Order of Operations (BIDMAS)
---------------------------------------------------------------
- Python follows BIDMAS: Brackets, Indices, Division/Multiplication, Addition, Subtraction
"""

# Examples:
print(2 + 3 * 4)       # 14 (multiplication first)
print((2 + 3) * 4)     # 20 (brackets first)
print(10 - 2 ** 2)     # 6 (exponent before subtraction)

# Task 5:
# - Write 3 calculations that give different results depending on brackets
# - Print each result

"""
---------------------------------------------------------------
Rounding Numbers
---------------------------------------------------------------
- round(number, decimals) rounds to a given number of decimal places
- int() removes decimals (truncates)
"""

# Examples:
print(round(3.14159, 2))  # 3.14
print(round(2.718, 1))    # 2.7
print(int(3.9))           # 3

# Task 6:
# - Store 3.56789 in a variable
# - Print it rounded to 2 decimal places
# - Print it rounded to 0 decimal places
# - Print it as an integer

"""
---------------------------------------------------------------
Combination Tasks
---------------------------------------------------------------
Now use everything together: variables, conversions, arithmetic, incrementing, order of operations, and rounding.
"""

# Task 7:
# - Store a variable for the radius of a sphere (float)
# - Calculate the volume using the formula: (4/3) * π * r^3
# - Use 3.14159 for π
# - Round the result to 2 decimal places
# - Print the volume in a full sentence

# Example setup (students fill in calculations):
radius = 6.0
pi = 3.14159

# Task 8 (Challenge):
# - Write a program that:
#   1. Stores your monthly pocket money/allowance in a variable
#   2. Increments it by 10% (as a raise) using x += ...
#   3. Subtracts 20 for expenses
#   4. Prints the final amount rounded to 2 decimal places

# Example setup (students fill in calculations):
allowance = 100.0
"""

---------------------------------------------------------------
Recap
---------------------------------------------------------------
- Today we revised variables, strings, and comments from Class 1.
- We learned:
  * Converting between data types
  * Arithmetic operations (+, -, *, /, //, %, **)
  * Incrementing and decrementing variables (x += 1, x -= 1)
  * Order of operations (BIDMAS)
  * Rounding numbers with round() and int()
- We combined these skills to solve practical problems.
"""
