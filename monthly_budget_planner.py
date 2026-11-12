print("================================")
print("     MONTHLY BUDGET PLANNER")
print("================================")

income = float(input("Enter your monthly income: Rs. "))

n = int(input("Enter number of expenses: "))

total_expense = 0

for i in range(n):
    print("\nExpense", i + 1)

    name = input("Enter expense name: ")
    amount = float(input("Enter amount: Rs. "))

    total_expense = total_expense + amount

balance = income - total_expense

print("\n========== BUDGET REPORT ==========")

print("Monthly Income: Rs.", income)
print("Total Expenses: Rs.", total_expense)
print("Remaining Balance: Rs.", balance)

if balance > 0:
    print("You have saved some money!")

elif balance == 0:
    print("Your entire income is used.")

else:
    print("Warning! You exceeded your budget.")

print("================================")
print("Thank you for using Budget Planner!")
