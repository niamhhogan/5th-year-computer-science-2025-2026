"""
---------------------------------------------------------------
5th Year Computer Science – Class 3: Input Statements & Debugging
---------------------------------------------------------------



---------------------------------------------------------------
Input Statements
---------------------------------------------------------------
- The input() function lets the user type something into the program.
- By default, input() always returns a string (text). 
- If we want a number, we must convert it using int() or float().
"""

# Examples:
name = input("Enter your name: ")
print("Hello,", name)

age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

height = float(input("Enter your height in metres: "))
print("Your height is", height, "metres.")

# Task 1:
# Ask the user to input their favourite colour and print a sentence with it
# Ask the user to input their age (convert to int) and print what their age will be in 5 years


"""
---------------------------------------------------------------
Debugging Practice – Broken Programs
---------------------------------------------------------------
Each of these small programs has one or more errors. 
Copy the code, try to run it, read the error messages, and fix the problems.
"""
#Debugging Task
#  A 
# age = input("Enter your age: "  
# print("Next year you will be", age + 1)  

# B 
# length = 5
# width = 3
# area = lenght * width   
# print("The area is", area)

# C 
# Name = input("Enter your name: )
# Print("Hello", name)   

# D 
# length = 10
# width = 4
# perimeter = length * width   
# print("The perimeter is", perimeter)

# E
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# total = num1 + num2  
# print("The total is:", total)

# F 
# result = 10 / 3
# print("Rounded result is" round(result, 2))  

# G
# radius = float(input("Enter the radius: ")) 
# pi = 3.14159
# volume = 4/3 * pi * r**3   
# print("The volume is:" volume)   


"""
---------------------------------------------------------------
Compiling Several Lines of Code
---------------------------------------------------------------
- A program often needs multiple steps: 
  1. Input values
  2. Process/calculations
  3. Output results
"""

# Example: Area of a rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print("The area of the rectangle is", area)

# Task 2:
# - Write a program to calculate the perimeter of a rectangle
# - Formula: perimeter = 2 * (length + width)
# - Ask the user for length and width (float)
# - Print the result with a clear message


"""
---------------------------------------------------------------
Consolidation Tasks
---------------------------------------------------------------
Now use everything from Classes 1, 2, and 3 (variables, input, conversion, arithmetic, order of operations, rounding).
"""

# Task 3:
# - Ask the user for two numbers (floats)
# - Print their sum, difference, product, and quotient (rounded to 2 decimals)

# Task 4:
# - Ask the user for the radius of a sphere (float)
# - Calculate the volume using (4/3) * π * r^3 (use π = 3.14159)
# - Print the result rounded to 2 decimal places

# Task 5 (Challenge):
# - Ask the user how much money they have saved
# - Increase it by 5% interest (use x *= 1.05)
# - Subtract 50 for expenses
# - Print the final balance rounded to 2 decimal places


"""
---------------------------------------------------------------
Recap
---------------------------------------------------------------
- Today we learned about:
  * input() for user input (always returns a string)
  * Converting input into int or float for calculations
  * Debugging broken code (syntax and logic errors)
  * Compiling multi-line programs with input, processing, and output
- We then used all skills together in practical problems.
"""
