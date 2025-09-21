"""
5th Year Computer Science — Loops & Lists (Revision + Practice)

Learning Intentions:
- Understand when and how to use for loops and while loops.
- Use range() correctly (start, stop, step) and avoid off-by-one errors (OBOE).
- Create and manipulate lists (create, index, slice, update, add, remove).
- Iterate over lists using for loops and while loops.
- Combine loops with lists to solve practical problems.

"""


#RECAP: While loops
# -------- While loops ----------
# While loops repeat WHILE a condition is True.
# Use when you don't know exactly how many iterations you'll need.
print("While loop example (count up to 5):")
count = 1
while count <= 5:
    print(count, end=" ") #end=" " creates a space between the values going across
    count += 1
print()


#FOR LOOPS
# -------- For loops with range() ----------
# range(start, stop) goes from start up to BUT NOT INCLUDING stop.
# range(start, stop, step)

print("For loop with range(start, stop):")
for i in range(1, 5):  # prints 1, 2, 3, 4
    print(i)


print("For loop with range(start, stop, step):")
for n in range(2, 11, 2):  # prints even numbers 2..10
    print(n)
    
print("Using step to count backwards")
for x in range(10,0,-1):
    print(x)


# -------- Off-by-one error (OBOE) ----------
# OBOE = Off-By-One Error: loop runs one time too many or too few,


print("With error (missing 5):")
for i in range(1, 5):  # should have used 6 to include 5
    print(i)
    
print("Correct (includes 5):")
for i in range(1, 6):
    print(i)





# -------- Student Tasks: Loops ----------
# Print multiples of 3 from 3 to 30 inclusive using a for loop.
# Using a while loop, keep doubling a number starting at 1 until it goes past 1000. Print each value.
# Input validation with while: keep asking for a number between 1 and 10 until the user enters one.






#LISTS 
# A list stores multiple items in order. Lists are mutable (you can change them).
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
print(type(fruits)) #returns data type: lists

# Indexing
print("First item:", fruits[0])       # "apple"
print("Last item:", fruits[-1])      # "cherry"

# Slicing: list[start:stop] → items from start up to (but not including) stop
print(fruits[0:2])              # ["apple", "banana"]
print(fruits[:2])                # ["apple", "banana"]
print(fruits[1:])                # ["banana", "cherry"]

# Updating items
fruits[1] = "blueberry"
print("After update index 1 → 'blueberry':", fruits)

# Adding items
fruits.append("date")        # add to end
fruits.insert(1, "banana")   # insert at position 1
print("After append + insert:", fruits)

# Removing items
fruits.remove("banana")  # removes first matching "banana"
print("After remove('banana'):", fruits)

# Checking membership and length
print("apple" in fruits) #returns True or False
print("List length:", len(fruits)) #returns the amount of items in the list

#Sorting lists
list_numbers=[3, 7, 18, -5, 90, 2, 11]
list_numbers.sort() #changes the original list
print(list_numbers)

list_2=[3,5,8,20,41,-4]
list_2.sort(reverse=True)
print(list_2)

list_3=[1,7,4,3,8]
print(sorted(list_3)) #only sorts it to print, but doesn't change the original list
print(list_3)


#LOOPS & LISTS

#example 1
pet_list=[] #initialising an empty list

total_pets=int(input("How many pets do you have?"))

if total_pets>0:
    for p in range(total_pets):
        name=input("Enter pet's name: ")
        pet_list.append(name)
        
    print(f"The names of your pets are: {pet_list}")

else:
    print("You have no pets")
    
