"""
5th Year Computer Science — Python Test Revision (Solutions)

This file mirrors the practice revision and includes:
- Brief model answers for THEORY (in comments)
- Fixed versions for DEBUGGING
- Reference implementations for PRACTICAL TASKS

Note: There are many valid ways to solve these. This shows clear, first-test-level solutions.
"""

# ============================================================
# A) THEORY — model answers (comments)
# ============================================================

# Q1. What is Python and why is it useful to learn?
# A1: A high-level, general-purpose programming language. It’s readable and has lots of libraries,
#     so it’s good for learning, automation, data, web, games, etc.

# Q2. What is an IDE? Give one example.
# A2: Integrated Development Environment — software that helps you write/run/debug code.
#     Examples: Thonny, PyCharm, VS Code, IDLE.

# Q3. Which data type is each of the following?
#   a) 42            -> int
#   b) "42"          -> str
#   c) 3.14          -> float
#   d) True          -> bool
#   e) [1, 2, 3]     -> list

# Q4. What does type casting mean? Show how to convert "42" into an integer.
# A4: Converting a value from one type to another. Example: int("42") -> 42

# Q5. Explain the difference between = and == in Python.
# A5: = assigns a value to a variable; == compares two values for equality.

# Q6. How does range(start, stop) work in a for loop? Which value is excluded?
# A6: Starts at 'start' and goes up to but does NOT include 'stop'; the stop value is excluded.

# Q7. What is an off-by-one error? Give a short example.
# A7: When a loop runs one time too many or too few (e.g., range(1,5) prints 1..4, missing 5).

# Q8. word = "hello"; print(word[1:4])  What will this output, and why?
# A8: "ell" — slice takes index 1 up to but NOT including index 4 (h,e,l,l,o).

# Q9. Lists are mutable. What does that mean?
# A9: They can be changed in place (e.g., append, remove, assign to an index).


# ============================================================
# B) DEBUGGING — fixed code
# ============================================================

print("\n--- DEBUGGING (Solutions) ---")

# B1) Input and numbers
print("\nB1) Input and numbers (solution)")
a = input("Enter a number: ")
b = input("Enter another number: ")
try:
    a_num = float(a)
    b_num = float(b)
    print("Sum is", a_num + b_num)
except ValueError:
    print("Please enter valid numbers.")

# B2) Conditional check
print("\nB2) Conditional check (solution)")
x = 10
if x == 10:
    print("Ten")

# B3) While loop increment
print("\nB3) While loop increment (solution)")
count = 1
while count <= 5:
    print(count)
    count += 1

# B4) Case-insensitive comparison
print("\nB4) Case-insensitive comparison (solution)")
word = "python"
guess = input("Type python: ")
if guess.lower() == word:
    print("Correct")
else:
    print("Wrong")

# B5) Sorting
print("\nB5) Sorting (solution)")
nums = [4, 2, 9, 1]
# In-place:
nums_copy = nums[:]      # keep original
nums_copy.sort()
print("In-place sorted:", nums_copy)
print("Original stays:", nums)
# Sorted copy:
print("sorted() copy:", sorted(nums))


# ============================================================
# C) PRACTICAL TASKS — reference solutions
# ============================================================

print("\n--- PRACTICAL TASKS (Solutions) ---")

# C1) Variables, input, operators
print("\nC1) Variables, input, operators (solution)")
x = input("Enter first integer: ")
y = input("Enter second integer: ")
try:
    xi = int(x)
    yi = int(y)
    print("Sum:", xi + yi)
    print("Difference:", xi - yi)
    print("Product:", xi * yi)
    print("Remainder (xi % yi):", xi % yi if yi != 0 else "undefined (division by zero)")
except ValueError:
    print("Please enter valid integers.")

# C2) If/elif/else
print("\nC2) If/elif/else (solution)")
age_txt = input("Enter your age: ")
try:
    age = int(age_txt)
    if age < 13:
        print("Child")
    elif age <= 17:
        print("Teen")
    else:
        print("Adult")
except ValueError:
    print("Please enter a valid number.")

# C3) Strings
print("\nC3) Strings (solution)")
full_name = input("Enter your full name: ")
print("Lowercase:", full_name.lower())
print("Uppercase:", full_name.upper())
# Capitalise each word:
parts = full_name.split()
caps = [p.capitalize() for p in parts]
proper = " ".join(caps)
print("Capitalised:", proper)
# First/last character (guard empty):
if len(full_name) > 0:
    print("First char:", full_name[0])
    print("Last  char:", full_name[-1])
# Slice 1..3 (indexes 1,2,3) if long enough:
if len(full_name) >= 4:
    print("Chars 1..3:", full_name[1:4])

# C4) For loop
print("\nC4) For loop (solution)")
for i in range(1, 11):
    print(i, end=" ")
print()

# C5) While loop
print("\nC5) While loop (solution)")
resp = ""
while resp.lower() != "yes":
    resp = input('Type "yes": ')
print("Thank you")

# C6) Lists
print("\nC6) Lists (solution)")
pet_list = []
try:
    total_pets = int(input("How many pets do you have? "))
    if total_pets > 0:
        for _ in range(total_pets):
            name = input("Enter pet's name: ")
            pet_list.append(name)
        print("Full list:", pet_list)
        print("Names on one line:", end=" ")
        for pet in pet_list:
            print(pet, end=" ")
        print()
        if len(pet_list) >= 1:
            print("First pet:", pet_list[0])
            print("Last pet:", pet_list[-1])
    else:
        print("No pets recorded.")
except ValueError:
    print("Please enter a valid integer.")

# C7) List statistics
print("\nC7) List statistics (solution)")
numbers = []
print("Enter 5 numbers:")
while len(numbers) < 5:
    v = input(f"Number {len(numbers)+1}: ")
    try:
        numbers.append(float(v))
    except ValueError:
        print("Please enter a valid number.")
# Manual sum/min/max
total = 0
min_v = numbers[0]
max_v = numbers[0]
for n in numbers:
    total += n
    if n < min_v:
        min_v = n
    if n > max_v:
        max_v = n
print("Sum:", total, "Min:", min_v, "Max:", max_v)

# C8) Sorting names
print("\nC8) Sorting names (solution)")
raw = input('Enter 4 names (comma-separated), e.g. "Aoife, Alex, Jordan, Sam": ')
names = [s.strip() for s in raw.split(",") if s.strip() != ""]
# Case-insensitive sorted copy:
print("Case-insensitive sorted copy:", sorted(names, key=str.lower))
# In-place reverse alphabetical:
names.sort(reverse=True, key=str.lower)
print("Original list sorted in place (reverse, case-insensitive):", names)

print("\n--- End of Solutions File ---")
