"""
---------------------------------------------------------------
5th Year Computer Science – Class 4: Conditional Statements
---------------------------------------------------------------

Learning Intentions:
From this lesson the students will be able to:
- Understand what conditional statements are
- Write programs that make decisions using if/else
- Use comparison operators to control program flow
- Combine input, arithmetic, and conditionals to solve problems
- Debug code with logical errors in decision-making

Learning Outcomes:
LO 1.1 Students should be able to describe a systematic process for solving problems and making decisions
LO 1.3 Students should be able to solve problems using logic
LO 1.22 Students should be able to read, write, test, and modify computer programs
LO 2.20 Students should be able to identify and fix/debug warnings and errors in computer code and modify as required
"""
"""
---------------------------------------------------------------
Introduction to Conditional Statements
---------------------------------------------------------------
- Conditional statements allow programs to make decisions.
- Python uses:
    if        → run code only if a condition is true
    else      → run code if the condition is false
    elif      → test another condition if the first one is false

Comparison operators:
    ==  equals
    !=  not equal to
    >   greater than
    <   less than
    >=  greater than or equal to
    <=  less than or equal to
"""

# Example 1: Basic if/else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# Example 2: if / elif / else
grade = int(input("Enter your mark (0–100): "))
if grade >= 70:
    print("Distinction")
elif grade >= 50:
    print("Pass")
else:
    print("Fail")

# Task 1:
# - Ask the user for a number.
# - If it is greater than 10, print "Big number".
# - Otherwise, print "Small number".

"""
---------------------------------------------------------------
Debugging Conditional Statements
---------------------------------------------------------------
Find and fix the mistakes in these programs.
"""

# A
# number = int(input("Enter a number: "))
# if number = 10:
#     print("Number is 10")

# B
# age = int(input("Enter your age: "))
# if age > 18
#     print("Over 18")
# else
#     print("18 or under")

# C
# mark = int(input("Enter your exam mark: "))
# if mark >= 40:
#     print("Pass")
# elif mark < 40:
#     print("Fail")
# else:
#     print("This should never happen")

"""
---------------------------------------------------------------
Combining Input, Arithmetic, and Conditionals
---------------------------------------------------------------
"""

# Example: Even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("That number is even.")
else:
    print("That number is odd.")

# Task 2:
# - Ask the user for a number.
# - If it is divisible by 5, print "Multiple of 5".
# - Otherwise, print "Not a multiple of 5".


"""
---------------------------------------------------------------
Random Numbers with Conditionals
---------------------------------------------------------------
"""

import random
dice = random.randint(1, 6)
print("You rolled:", dice)

if dice == 6:
    print("You got the highest number!")
else:
    print("Better luck next time.")

# Task 3:
# - Generate a random number between 1 and 100.
# - If it is above 50, print "High number".
# - Otherwise, print "Low number".


"""
---------------------------------------------------------------
Consolidation Tasks
---------------------------------------------------------------
"""

# Task 4:
# - Ask the user for two numbers.
# - Print which number is bigger, or if they are equal.

# Task 5:
# - Ask the user to input a mark (0–100).
# - Print "Distinction" if >= 70, "Pass" if >= 40, otherwise "Fail".

# Task 6:
# - Ask the user for their age.
# - If age < 13, print "Child".
# - If age is between 13 and 19, print "Teenager".
# - Otherwise, print "Adult".

# Task 7 (Challenge):
# - Generate a random number between 1 and 10.
# - Ask the user to guess the number.
# - If the guess matches, print "Correct!".
# - Otherwise, print "Wrong, the number was X".


"""
---------------------------------------------------------------
Recap
---------------------------------------------------------------
- Today we learned about conditional statements (if, elif, else)
- We used comparison operators (==, !=, >, <, >=, <=)
- We debugged broken conditional code
- We combined input, arithmetic, random numbers, and decisions
- We finished with tasks that required making programs respond differently
  depending on the user input or random events
"""
