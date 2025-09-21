# Task 1:
# - Ask the user to input their favourite colour and print a sentence with it
# - Ask the user to input their age (convert to int) and print what their age will be in 5 years

fav_colour=input("What is your favourite colour?")
print("Your favourite colour is", fav_colour, ", great choice")

user_age=int(input("Enter your age:"))
print("In 5 years you will be", user_age+5, "years old")

# Task 2:
# - Write a program to calculate the perimeter of a rectangle
# - Formula: perimeter = 2 * (length + width)
# - Ask the user for length and width (float)
# - Print the result with a clear message

length=float(input("Enter length of rectangle:"))
width=float(input("Enter width of rectangle:"))
perimeter=2*(length+width)
print("The perimeter of the rectangle is:", perimeter, "units")


# Task 3:
# - Ask the user for two numbers (floats)
# - Print their sum, difference, product, and quotient (rounded to 2 decimals)

num1=float(input("Pick a number"))
num2=float(input("Pick another number"))
print("Your numbers are:",num1, "and", num2)
print("The sum is", num1+num2, "\nThe difference is:", num1-num2,"\nThe product is:", num1*num2)
print("The quotient is:", round(num1/num2, 2)) #i've just done this on a new line as the last one was getting long


# Task 4:
# - Ask the user for the radius of a sphere (float)
# - Calculate the volume using (4/3) * π * r^3 (use π = 3.14159)
# - Print the result rounded to 2 decimal places

radius=float(input("Enter the radius of a sphere: "))
pi=3.14159
volume=(4/3)*pi*(radius**3)
print("The volume of a sphere with radius of", radius, "is", round(volume, 2), "units cubed")

# Task 5:
# - Ask the user how much money they have saved (float)
# - Increase it by 5% interest (use x *= 1.05)
# - Subtract 50 for expenses
# - Print the final balance rounded to 2 decimal places

saved=float(input("Enter the amount of money saved: "))
amount1=saved*1.05
amount2=amount1-50
print("The final balance is:", round(amount2, 2), "Euro")

# Task 6:
# - Generate two random integers between 1 and 10
# - Print them out
# - Multiply them together and print the result
# - Divide the first number by the second and round to 2 decimal places

import random

num_1=random.randint(1,10)
num_2=random.randint(1,10)
print("The two random numbers generated are:", num_1, "and", num_2)
print("Multiplied together:", num_1*num_2)
print("Divided (to two decimal places):", round(num_1/num_2, 2))

# Task 7:
# - Ask the user for 3 test scores (floats)
# - Calculate the average
# - Round the result to 1 decimal place
# - Print the average score

test1=float(input("Enter the result of test 1:"))
test2=float(input("Enter the result of test 2:"))
test3=float(input("Enter the result of test 3:"))
average=(test1+test2+test3)/3
average_rounded=round(average, 1)
print("The average test result is:", average_rounded)
