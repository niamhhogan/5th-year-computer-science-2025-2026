"""
---------------------------------------------------------------
5th Year Computer Science – Class 6: Strings & Boolean Logic
---------------------------------------------------------------

Learning Intentions:
From this lesson the students will be able to:
- Recall and apply input statements and conditional statements
- Understand Boolean logic (and, or, not)
- Use Python string operations and methods
- Work with string indexing, slicing, and substrings
- Check for the presence and location of substrings
- Apply these skills in practical coding tasks
"""

"""
---------------------------------------------------------------
Recap – Input Statements and Conditionals
---------------------------------------------------------------
"""

# Example 1 – Recap of input + if/else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# Task 1:
# - Ask the user for their favourite colour
# - If it equals "blue", print "Nice choice!"
# - Otherwise, print "That’s a good colour too!"

# Question: Why do we use int() when asking for age but not for colour?


# Example 2 – Boolean logic with and/or/not
mark = int(input("Enter your mark: "))
if mark >= 40 and mark < 70:
    print("Pass")
elif mark >= 70:
    print("Distinction")
else:
    print("Fail")

# Question: What is the difference between using "and" and "or" in a condition?
# Question: What does the keyword "not" do in Python? Try writing an example.


"""
---------------------------------------------------------------
String Basics – Combining and Repeating Strings
---------------------------------------------------------------
"""

# Example 1 – Repetition and concatenation
word = "Hi"
print(word * 3)           # HiHiHi
print(word + " there!")   # Hi there!

# Task 2:
# - Create a variable with your name
# - Print it 5 times using *

# Question: What is the difference between word * 3 and word + word + word?


"""
---------------------------------------------------------------
Changing Case – capitalize, upper, lower
---------------------------------------------------------------
"""

msg = "hello world"
print(msg.capitalize())   # Hello world
print(msg.upper())        # HELLO WORLD
print(msg.lower())        # hello world

# Task 3:
# - Ask the user to type in their school name
# - Print it in all uppercase
# - Print it in all lowercase

# Question: Why might we want to convert a string to lowercase before comparing it?


"""
---------------------------------------------------------------
Removing Extra Spaces – strip()
---------------------------------------------------------------
"""

greeting = "   hello   "
print(greeting.strip())   # removes spaces at start and end

# Task 4:
# - Ask the user to enter a word with spaces around it
# - Remove the spaces and print the result

# Question: Does strip() remove spaces from the middle of the word?


"""
---------------------------------------------------------------
Length of a String – len()
---------------------------------------------------------------
"""

text = "Computer Science"
print(len(text))   # 16

# Task 5:
# - Ask the user for their favourite hobby
# - Print how many letters it has

# Question: Why is it useful to know the length of a string?


"""
---------------------------------------------------------------
Indexing – Accessing Individual Characters
---------------------------------------------------------------
"""

word = "Python"
print(word[0])    # P (first character)
print(word[1])    # y (second character)
print(word[-1])   # n (last character)

# Task 6:
# - Create a variable with your name
# - Print the first letter and the last letter

# Question: What happens if you try to access an index that is too large?


"""
---------------------------------------------------------------
Slicing – Extracting Substrings
---------------------------------------------------------------
"""

phrase = "I love Python programming"
print(phrase[0:6])   # I love
print(phrase[7:13])  # Python
print(phrase[:6])    # I love (start to 5)
print(phrase[7:])    # Python programming (7 to end)

# Task 7:
# - Ask the user to enter a sentence
# - Print the first 5 letters
# - Print everything from the 5th character onwards

# Question: What does phrase[::2] do? Try it and see.


"""
---------------------------------------------------------------
Substring Checks – "in" and find()
---------------------------------------------------------------
"""

phrase = "Python is great for learning."
print("Python" in phrase)         # True
print("Java" in phrase)           # False
print(phrase.find("great"))       # 10 (index where "great" starts)
print(phrase.find("Java"))        # -1 (not found)

# Task 8:
# - Ask the user to type a sentence
# - Check if the word "school" is in the sentence (print True/False)
# - Print the index of where "school" starts (if present)

# Question: What is the difference between using "in" and using find()?


"""
---------------------------------------------------------------
Consolidation Tasks
---------------------------------------------------------------
"""

# Task 9:
# - Ask the user to enter their first name
# - Print a message saying how many letters it has
# - Print the name in uppercase

# Task 10:
# - Ask the user for their favourite movie title
# - Remove any extra spaces around it
# - Print the title in lowercase
# - Print the first 3 letters of the title

# Task 11:
# - Ask the user for a sentence
# - Print the length of the sentence
# - Print the sentence in all capitals
# - Print the last 5 characters of the sentence

# Task 12 (Challenge):
# - Ask the user for a sentence
# - Check if the word "Python" is in the sentence
# - If it is, print the index of where it starts
# - Print the sentence again but in lowercase with spaces removed from the ends


"""
---------------------------------------------------------------
Recap
---------------------------------------------------------------
- Reviewed input() and conditional statements with Boolean logic
- Worked with string operations:
  * repetition (*), concatenation (+)
  * capitalize(), lower(), upper(), strip()
  * len(), indexing, slicing
  * substring checks with "in" and find()
- Applied these in practical tasks and challenges
"""
