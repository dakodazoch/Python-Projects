import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os

FILE_NAME = "data.csv"

# --- Create file if it doesn't exist ---
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])
    df.to_csv(FILE_NAME, index=False)

def add_transaction():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g. Food, Rent, Salary): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount (use negative for expenses): "))
    
    new_data = pd.DataFrame([[date, category, description, amount]], 
                            columns=["Date", "Category", "Description", "Amount"])
    
    df = pd.read_csv(FILE_NAME)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    
    print("✅ Transaction added successfully!\n")

def view_summary():
    df = pd.read_csv(FILE_NAME)
    print("\n--- Account Summary ---")
    print(df.tail())  # show last few transactions
    
    total_income = df[df["Amount"] > 0]["Amount"].sum()
    total_expense = df[df["Amount"] < 0]["Amount"].sum()
    balance = total_income + total_expense
    
    print(f"\nTotal Income: ${total_income:.2f}")
    print(f"Total Expense: ${abs(total_expense):.2f}")
    print(f"Current Balance: ${balance:.2f}\n")
    
def visualize_spending():
    df = pd.read_csv(FILE_NAME)
    expenses = df[df["Amount"] < 0].groupby("Category")["Amount"].sum().abs()
    
    if expenses.empty:
        print("No expenses to visualize yet.")
        return
    
    expenses.plot(kind="pie", autopct="%1.1f%%", figsize=(6,6))
    plt.title("Spending by Category")
    plt.show()

def main():
    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Visualize Spending")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            visualize_spending()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
