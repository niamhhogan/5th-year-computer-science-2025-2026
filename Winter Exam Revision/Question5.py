"""
Question 5 – Discount Card Checker 

Starting Code: 

# Student name: 

discount_card_list = [] 
 

(i) A clothing store offers a 10% discount to customers who have a store discount card. 
The names of cardholders are shown below: 
Aoife, Chloe, Adam, Jack, Erin, Michael, Holly, Ella, Sean, Eoin, Katie, Leah 
Add these names to the list called discount_card_list. 

(ii) Modify the code so that: 
a. It asks the user to enter their name. 
b. Check if their name is in the list discount_card_list. 

If it is, display "You qualify for the 10% discount." 

If not, display "You do not have a store discount card." 

(iii) If the customer is not on the list, ask if they would like to sign up for one (y/n). 

If yes, add their name to the list and display the updated list sorted alphabetically. 

Use .lower() and .strip() on inputs to avoid spacing and capitalisation errors.
"""
#SOLUTION

#part (i): This program checks if a customer has a store discount card and allows new customers to sign up

# Student name:

discount_card_list = ["Aoife", "Chloe", "Adam", "Jack", "Erin", 
                      "Michael", "Holly", "Ella", "Sean", "Eoin", 
                      "Katie", "Leah"]

#part (ii)(a): Ask the user to enter their name
name = input("Please enter your name: ").strip().capitalize()

#part (ii)(b): Check if the name is in the discount card list
if name in discount_card_list:
    print("You qualify for the 10% discount.")
else:
    print("You do not have a store discount card.")

    #part (iii): Ask if they want to sign up
    signup = input("Would you like to sign up for one? (y/n): ").strip().lower()

    if signup == "y":
        discount_card_list.append(name)
        discount_card_list.sort()
        print("You have been added. Updated discount card list:")
        print(discount_card_list)
