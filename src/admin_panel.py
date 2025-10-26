import pandas as pd
from handeldata import userhandel

transactions_df = pd.read_csv("data/transactions.csv")
user_df = pd.read_csv("data/user.csv")

uh = userhandel.Userhandel()


class AdminPanel:
    def __init__(self):
        print("Welcome to the Admin Panel")
        # Admin functionalities would go here
        while True:
            print("1. Add User")  # take name,user_name,password,amount,limit as input
            print("2. Delete User")  # take username as input
            print("3. Deposit Funds")  # take username and amount as input
            print("4. View Transactions")  # take username as input
            print("5. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                uh.addUser()
            elif choice == "2":
                uh.deleteUser()
            elif choice == "3":
                uh.depositFunds()
            elif choice == "4":
                uh.viewTransactions()
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
