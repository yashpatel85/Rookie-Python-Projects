print("Welcome to the Tip Calculator!")

total_bill_amount = float(input("Enter the total amount that you need to pay: ₹"))

tip = int(input("What percentage of the tip would you like to give from the total amount?: "))
final_tip = tip / 100       #Converting the tip to percentage for further calculations. 

final_tip_amount = round(total_bill_amount * final_tip, 2)

final_bill_amount = total_bill_amount + final_tip_amount

total_bill_splitters = int(input("How many people are going to split the bill?: "))

amount_per_person = round(final_bill_amount / total_bill_splitters, 2) 

print(f"Your total bill with tip is ₹{final_bill_amount} and each person should to pay ₹{amount_per_person}.")
print("Thanks for Coming, Visit us Again Soon!!!")