"""
Question 4 – Library Membership Checker 

Starting Code: 

# Student name: 

library_members = [] 
 

(i) The local library keeps a list of members who are currently registered. The members’ names are shown below: 
Sarah, John, Emma, Aidan, Grace, Daniel, Laura, Sophie, Ben, Megan 
Place these names into the list called library_members. 

(ii) Modify the code so that: 
a. It asks the user to enter the name of the person who wants to borrow a book. 
b. Use an if statement to check if the person is in the library_members list. If they are, output: 
"[Name] is a registered library member." 
c. If the person is not in the list, output: 
"[Name] is not a registered library member." 

(iii) If the person is not on the list, ask if they would like to register as a new member (y/n). 

If they choose yes ("y"), add their name to the library_members list. 

Display the updated list in alphabetical order.
"""
#SOLUTION

#part (i): This program checks if a person is a registered library member and allows new members to be added

# Student name:

library_members = ["Sarah", "John", "Emma", "Aidan", "Grace", "Daniel", "Laura", "Sophie", "Ben", "Megan"]

#part (ii)(a): Ask the user to enter the name of the person who wants to borrow a book
name = input("Enter the name of the person who wants to borrow a book: ").strip().capitalize()

#part (ii)(b) and (c): Check if the person is a library member
if name in library_members:
    print(f"{name} is a registered library member.")
else:
    print(f"{name} is not a registered library member.")

    #part (iii): Ask if they would like to register as a new member
    register = input("Would you like to register as a new member? (y/n): ").strip().lower()

    if register == "y":
        library_members.append(name)
        library_members.sort()
        print("Member added. Updated list:")
        print(library_members)
