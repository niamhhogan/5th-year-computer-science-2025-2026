"""
5th Year Computer Science:
Class 8: Iteration (While loops)

🎯 Learning Intentions
- Understand what a while loop is and how it works.
- Use while loops to repeat code while a condition is True.
- Recognise and avoid the OBOE (Off-By-One Error).
- Apply while loops to real problems like guessing games and menus.

📝 What is a while loop?
- A while loop is a type of iteration (repetition) in programming.
- It keeps running the same block of code again and again
  as long as a condition is TRUE.

📝 When are while loops used?
- When you don't know exactly how many times you want to repeat something.
- Example: asking the user to guess a number until they get it right.
- Example: keep showing a menu until they choose 'quit'.

⚠️ Warning:
- If the condition is always TRUE, the loop will run forever (infinite loop).
- You must have something inside the loop that will eventually make it stop.

⚠️ OBOE (Off-By-One Error):
- A common error when using loops.
- Happens when your loop runs one time too many or one time too few.
- Example: using <= 10 instead of < 10 could make the loop run 11 times.
"""

# ---------------------------------
# Example 1: Simple counter
# ---------------------------------
print("Example 1: Counting up")
count = 1  # initialising the count variable
while count <= 5:
    print("Count is", count)
    count = count + 1  # incrementing by 1
print("Loop finished!\n")

# 💻 Student Tasks
# - Change the code to count from 5 up to 10.
# - Change it to count in steps of 2 (2, 4, 6, 8, 10).
# - Make it count from 10 down to 1. (Hint: subtract 1 each time)


# ---------------------------------
# Example 2: Asking until correct answer
# ---------------------------------
print("Example 2: Asking for the password")
password = ""  # initialising an empty variable
while password != "secret":
    password = input("Enter the password: ")
print("Correct!\n")

# 💻 Student Tasks
# - Change the correct password to your name.
# - Make it say "Too short!" if the user types fewer than 3 letters.
# - Count how many tries it takes to get it correct.


# ---------------------------------
# Example 3: Random Number Guessing Game
# ---------------------------------
import random

comp_num = random.randint(1, 10)
user_num = 0

while comp_num != user_num:
    user_num = int(input("Enter a number between 1 and 10: "))
    if user_num > comp_num:
        print("Too high, guess again")
    elif user_num < comp_num:
        print("Too low, guess again")
    else:
        print("Correct, well done!")

# 💻 Student Tasks
# - Make it pick a number between 1 and 20 instead.
# - Add a counter to show how many guesses it took.
# - Make it give a hint if the user is only 1 away ("Very close!")


# ---------------------------------
# Example 4: Options (Simple Calculator)
# ---------------------------------
print("Calculator Program")

option = 0
while option != 5:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\nMenu")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Quit")

    option = int(input("Please enter the number of the function you want to use: "))

    if option == 1:
        print(f"{a}+{b}={a+b}")

    elif option == 2:
        print(f"{a}-{b}={a-b}")

    elif option == 3:
        print(f"{a}x{b}={a*b}")

    elif option == 4:
        if b != 0:
            print(f"{a}/{b}={a/b}")
        else:
            print("Cannot divide by zero!")

    elif option == 5:
        print("Goodbye!")

    else:
        print("Invalid option, please choose 1–5")

# 💻 Student Tasks
# - Move the "enter first/second number" inputs inside each operation instead of before the menu.
# - Add a 6th option for modulus (%) and a 7th for powers (**).
# - Prevent the user from typing negative numbers.


# ---------------------------------
# Example 5: Infinite loop with break
# ---------------------------------
while True:  # This will keep running forever unless we use 'break'

    # Ask the user for input
    answer = input("Type 'stop' to end the loop: ").lower()

    # If the user types "stop", break out of the loop
    if answer == "stop":
        print("Loop stopped!")
        break  # This ends the loop completely

    # If they typed something else, just show what they typed
    print("You typed:", answer)

# This line only runs after the loop has ended
print("Program finished")


# ---------------------------------
# 📝 Student Tasks (End of Class)
# ---------------------------------

# Task 1:
# Make a while loop that counts down from 10 to 1 and then prints "Go!"

# Task 2:
# Write a while loop that keeps asking the user to type "yes"
# and only stops when they do.

# Task 3:
# Create a simple menu that shows 3 options:
# 1) Say Hello
# 2) Say Goodbye
# 3) Quit
# Keep showing the menu until the user types 3.

# Task 4:
# Create a number-guessing game where the computer picks a number from 1 to 50.
# Give the user hints (too high/too low) until they guess it right.

# Task 5:
# Challenge: Create a password system.
# The user must type the correct password.
# If they get it wrong 3 times, the program prints "Too many tries" and stops.




