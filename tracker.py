import pandas as pd
from datetime import datetime
import os

FILENAME = "expenses.csv"

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Add a note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")

    # Create a DataFrame with one new row
    new_data = pd.DataFrame([[date, amount, category, note]])

    # If file exists, append; else create with columns
    if os.path.exists(FILENAME):
        new_data.to_csv(FILENAME, mode='a', index=False, header=False)
    else:
        new_data.columns = ["Date", "Amount", "Category", "Note"]
        new_data.to_csv(FILENAME, index=False)
    
    print("✅ Expense added!")

def view_expenses():
    if os.path.exists(FILENAME):
        df = pd.read_csv(FILENAME, names=["Date", "Amount", "Category", "Note"])
        print("\n--- All Expenses ---")
        print(df.to_string(index=False))
    else:
        print("No expenses found.")

def total_by_category():
    if os.path.exists(FILENAME):
        df = pd.read_csv(FILENAME, names=["Date", "Amount", "Category", "Note"])
        summary = df.groupby("Category")["Amount"].sum()
        print("\n--- Total by Category ---")
        print(summary)
    else:
        print("No data available.")

# Main menu
while True:
    print("\n💰 Expense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total by Category")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_by_category()
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
