print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill amount?\n"))
tip_percentage = int(input("What tip percentage would you like to give? (10, 12, 15, or 20)\n"))
num_of_people = int(input("How many people to split the bill with?\n"))
total_amt = 0.00

if (num_of_people == 0):
    total_amt = total_bill + (total_bill * (tip_percentage / 100))
    total_amt = round(total_amt, 2)
    print(f"You have to pay: ${total_amt}")
else:
    total_amt = (total_bill + (total_bill * (tip_percentage) / 100)) / num_of_people
    total_amt = round(total_amt, 2)
    print(f"Each person has to pay: ${total_amt}")