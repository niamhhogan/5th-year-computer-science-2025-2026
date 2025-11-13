"""
Question 1 – Pet Food Cost Calculator 
 

Starting Code: 

print("Welcome to the pet food cost calculator.\n") 
total_cost = 0 
items_count = 1 
price_of_item = float(input(f"Enter the price of item {items_count}: €")) 
total_cost += price_of_item 
print(f"You entered {items_count} item(s) and the total is €{total_cost}")

(i) Add a comment at the top to describe what the program does. 
 
(ii) Ask the user to enter their name and display a message such as: 
f"Order processed by: {name}" 
 
(iii) Use a while loop to ask how many types of pet food are being purchased. If a negative number is entered, display "Invalid number" and ask again. 
 
(iv) Use a for loop to enter the price of each pet food type and calculate the total cost. 
 
(v) Print the total cost using an f-string, rounded to two decimal places. 
 
(vi) Ask the user to enter the amount of money the customer is paying. 
 
(vii) Use if–else statements to display either: 
• f"Payment complete, change due: €{change}" 
• f"Not enough money, customer still owes: €{amount_owed}" 
"""

#SOLUTION

#part(i): This program calculates the total cost of pet food and shows the customer amount due


print("Welcome to the pet food cost calculator.\n")

#part (ii): use input statement to allow the user to enter their name
name=input("Please enter your name: ").strip().capitalize()
print(f"Order processed by: {name}")

#part (iii): using a while loop to get how many types of pet food are being purchased
while True:
    types=int(input("How many types of pet food are being purchased? "))
    if types < 0:
        print("Invalid number entered")
    else:
        break
    
#part (iv): use a for loop to enter the price for each item bought
total_cost=0

for i in range(1,types+1):
    price_of_item=float(input(f"Please enter the price of item {i}: €"))
    total_cost += price_of_item
    
#part (v): rounding to two decimal places and printing
total_cost=round(total_cost, 2)
print(f"The total cost is: €{total_cost}")

#part (vi): use input statement to ask for customers payment amount
payment=float(input("Enter the amount of money the customer is paying: €"))

#part (vii): using a conditional statement to check balance or changed owed
if payment >= total_cost:
    change=round(payment-total_cost,2)
    print(f"Payment complete. Your change is €{change}")
else:
    amount_owed=round(total_cost-payment,2)
    print(f"Not enough money, €{amount_owed} still due")
