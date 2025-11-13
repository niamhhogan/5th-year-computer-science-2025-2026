"""
Question 3 – Phone Credit Top-Up 
 

Starting Code: 

print("Welcome to the phone credit top-up system.\n") 

total_cost = 0 
 

(i) Add a comment at the top to describe what the program does. 
 
(ii) Ask the user to enter their name and print a message such as: 
f"Top-up processed by: {name}" 
 
(iii) Use a while loop to ask how many phones need to be topped up. If the number entered is less than 1, display "Invalid entry" and ask again. 
 
(iv) Use a for loop to ask for each customer’s top-up amount using: 
f"Enter the top-up amount for customer {i}: €" 
 
(v) Add each amount to the total. 
 
(vi) After all top-ups are entered, print the total amount due using an f-string. 
 
(vii) Ask how much money was collected from customers. 
 
(viii) Use if–elif–else statements to display one of the following messages: 
• f"All payments received. Change due: €{change}" 
• f"More money needed to cover top-ups. Amount owed: €{amount_owed}" 
• "Exact payment received. Thank you!" 
 
(ix) Round all values to two decimal places"""

#SOLUTION

#part (i): This program calculates the total cost of phone credit top-ups and checks if enough money was collected

print("Welcome to the phone credit top-up system.\n")

total_cost = 0

#part (ii): Ask the user to enter their name
name = input("Please enter your name: ").strip().capitalize()
print(f"Top-up processed by: {name}")

#part (iii): Ask how many phones need to be topped up, using a while loop
while True:
    phones = int(input("How many phones need to be topped up? "))
    if phones < 1:
        print("Invalid entry")
    else:
        break

#part (iv) and (v): Use a for loop to get each top-up amount and add to total
for i in range(1, phones + 1):
    amount = float(input(f"Enter the top-up amount for customer {i}: €"))
    total_cost += amount

#round total_cost
total_cost = round(total_cost, 2)

#part (vi): Print total amount due
print(f"The total amount due is: €{total_cost:.2f}")

#part (vii): Ask how much money was collected
collected = float(input("Enter the total amount of money collected: €"))
collected = round(collected, 2)

#part (viii): Compare collected amount to total cost
if collected > total_cost:
    change = round(collected - total_cost, 2)
    print(f"All payments received. Change due: €{change}")
elif collected < total_cost:
    amount_owed = round(total_cost - collected, 2)
    print(f"More money needed to cover top-ups. Amount owed: €{amount_owed}")
else:
    print("Exact payment received. Thank you!")
