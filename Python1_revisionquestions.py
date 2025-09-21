"""
5th Year Computer Science — Python Test Revision

First Test Preparation (Weeks 1–4)

Topics Covered:
- What is Python? What is an IDE?
- Data types and converting between them
- Variables and input statements
- Operators (+, -, *, /, //, %, **)
- Conditional statements (if/elif/else)
- Strings: indexing, slicing, .lower(), .upper(), .capitalize()
- Loops: while and for
- Lists: creating, indexing, adding, removing, iterating, sorting

INSTRUCTIONS:
- Answer THEORY in comments.
- Correct DEBUGGING snippets by writing your fixed version underneath.
- Complete PRACTICAL TASKS by writing your code in the given spaces.
- This revision is designed to prepare you for your FIRST TEST.
"""

# ============================================================
# A) THEORY — answer in comments
# ============================================================

# Q1. What is Python and why is it useful to learn?
# Your answer:

# Q2. What is an IDE? Give one example.
# Your answer:

# Q3. Which data type is each of the following?
#   a) 42
#   b) "42"
#   c) 3.14
#   d) True
#   e) [1, 2, 3]
# Your answer:

# Q4. What does type casting mean? Show how to convert "42" into an integer.
# Your answer:

# Q5. Explain the difference between = and == in Python.
# Your answer:

# Q6. How does range(start, stop) work in a for loop? Which value is excluded?
# Your answer:

# Q7. What is an off-by-one error? Give a short example.
# Your answer:

# Q8. word = "hello"; print(word[1:4])  
# What will this output, and why?
# Your answer:

# Q9. Lists are mutable. What does that mean?
# Your answer:


# ============================================================
# B) DEBUGGING — fix the code so it runs correctly
# ============================================================

print("\n--- DEBUGGING ---")

# B1) Input and numbers
print("\nB1) Input and numbers")
# Broken:
# a = input("Enter a number: ")
# b = input("Enter another number: ")
# print("Sum is", a + b)
# Task: Fix so numbers are added correctly, not joined as text.

# Write your fix here:


# B2) Conditional check
print("\nB2) Conditional check")
# Broken:
# x = 10
# if x = 10:
#     print("Ten")
# Task: Use the correct comparison operator.

# Write your fix here:


# B3) While loop increment
print("\nB3) While loop increment")
# Broken:
# count = 1
# while count <= 5:
#     print(count)
# Task: Fix so it prints 1..5 and then stops.

# Write your fix here:


# B4) Case-insensitive comparison
print("\nB4) Case-insensitive comparison")
# Broken:
# word = "python"
# guess = input("Type python: ")
# if guess == word:
#     print("Correct")
# else:
#     print("Wrong")
# Task: Accept "Python", "PYTHON", etc.

# Write your fix here:


# B5) Sorting
print("\nB5) Sorting")
# Broken:
# nums = [4, 2, 9, 1]
# print(nums.sort())
# Task: Show how to print the sorted list properly.

# Write your fix here:


# ============================================================
# C) PRACTICAL TASKS — write your code for each task
# ============================================================

print("\n--- PRACTICAL TASKS ---")

# C1) Variables, input, operators
print("\nC1) Variables, input, operators")
# Task: Ask the user for two integers. Print their sum, difference, product, and remainder.

# Write your solution here:


# C2) If/elif/else
print("\nC2) If/elif/else")
# Task: Ask the user for their age.
# - If under 13: print "Child"
# - If 13–17: print "Teen"
# - If 18 or older: print "Adult"

# Write your solution here:


# C3) Strings
print("\nC3) Strings")
# Task: Ask the user for their name.
# - Print the name in all lowercase, all uppercase, and capitalised.
# - Print the first and last character of the name.

# Write your solution here:


# C4) For loop
print("\nC4) For loop")
# Task: Use a for loop to print the numbers from 1 to 10 inclusive.

# Write your solution here:


# C5) While loop
print("\nC5) While loop")
# Task: Keep asking the user to type "yes" until they do.
# Then print "Thank you".

# Write your solution here:


# C6) Lists
print("\nC6) Lists")
# Task: Ask the user how many pets they have. 
# If > 0, input each pet’s name and store in a list.
# Print the full list, then print the names one by one using a loop.

# Write your solution here:


# C7) List statistics
print("\nC7) List statistics")
# Task: Make a list of 5 numbers. 
# Print the largest and smallest number in the list.

# Write your solution here:


# C8) Sorting names
print("\nC8) Sorting names")
# Task: Make a list of 4 names with mixed uppercase/lowercase.
# Print the list sorted alphabetically, ignoring case.

# Write your solution here:


print("\n--- End of Revision File ---")
