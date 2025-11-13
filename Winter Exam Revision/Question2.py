"""
Question 2 – Café Order Program 
 

Starting Code: 

print("Welcome to the café ordering system.\n") 

total_cost = 0 

print("All hot drinks cost €2.50 each.") 
 

(i) Add a comment describing what the program does. 
 
(ii) Ask the user to enter their name and print a message such as: 
f"Order taken by: {name}" 
 
(iii) Ask how many drinks the customer would like to buy. 
 
(iv) Use a while loop to make sure the number entered is greater than 0. 
 
(v) Use a for loop to calculate the total price of the drinks ordered. 
 
(vi) Ask if the customer wants a snack (yes or no). If yes, add €1.50 to the total. 
 
(vii) Print the total cost using an f-string, rounded to two decimal places. 
 
(viii) Ask for the customer’s balance and print either: 
• f"Order complete. Remaining balance: €{balance - total_cost}" 
• "Not enough funds to complete order."
"""

#SOLUTION

#part (i): This program calculates the total cost of a café order including drinks and optional snacks

print("Welcome to the café ordering system.\n")

total_cost = 0

print("All hot drinks cost €2.50 each.")

#part (ii): Ask the user to enter their name
name = input("Please enter your name: ").strip().capitalize()
print(f"Order taken by: {name}")

#part (iii): Ask how many drinks the customer would like to buy
drinks = int(input("How many drinks would the customer like to buy? "))

#part (iv): while loop to ensure number is greater than 0
while drinks <= 0:
    print("Number must be greater than 0.")
    drinks = int(input("How many drinks would the customer like to buy? "))

#part (v): for loop to calculate the total price of the drinks
for i in range(1, drinks + 1):
    total_cost += 2.50

#part (vi): Ask if the customer wants a snack
snack = input("Would the customer like a snack? (yes or no): ").strip().lower()

if snack == "yes":
    total_cost += 1.50

#part (vii): Print the total cost rounded to two decimal places
total_cost = round(total_cost, 2)
print(f"The total cost is €{total_cost:.2f}")

#part (viii): Ask for customer’s balance and check if they can pay
balance = float(input("Enter the customer’s balance: €"))

if balance >= total_cost:
    remaining = round(balance - total_cost, 2)
    print(f"Order complete. Remaining balance: €{remaining}")
else:
    print("Not enough funds to complete order.")
