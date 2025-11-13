#SOLUTION

#part (i): This program checks if a supplier is approved and allows new suppliers to be added

# Student name:

approved_suppliers = ["BrightTech", "GreenEnergy", "NovaParts", "EcoBuild", 
                      "SmartSource", "RapidTools", "AlphaSteel", "PrimePlastics", 
                      "SafeWear", "PolyTech", "AeroWeld", "BuildPro"]

#part (ii)(a): Ask the user to enter a supplier name
supplier = input("Enter the name of the supplier you wish to order from: ").strip()

#part (ii)(b): Check if the supplier is approved
if supplier in approved_suppliers:
    print("This supplier is approved for purchases.")
else:
    print("This supplier is not on the approved list.")

    #part (iii): Ask if they would like to add the supplier
    add_supplier = input("Would you like to add this supplier for future orders? (y/n): ").strip().lower()

    if add_supplier == "y":
        approved_suppliers.append(supplier)
        approved_suppliers.sort()
        print(f"{supplier} has been added to the approved supplier list.")
        print("Updated list:")
        print(approved_suppliers)
