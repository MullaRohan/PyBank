import pandas as pd
from handeldata.userhandel import Userhandel as uh
from handeldata.transaction_handel import Transaction as th


transactions_df = pd.read_csv("data/transactions.csv")
user_df = pd.read_csv("data/user.csv")


class AdminPanel:
    def __init__(self):
        print("Welcome to the Admin Panel")
        # Admin functionalities would go here
        while True:
            print("1. Add User")  # take name,user_name,password,amount,limit as input
            print("2. Delete User")  # take username as input
            print("3. Deposit Funds")  # take username and amount as input
            print("4. See User")
            print("5. View Transactions")  # take username as input
            print("6. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                uh.addUser()
            elif choice == "2":
                uh.deleteUser()
            elif choice == "3":
                uh.depositFunds()
            elif choice == "4":
                uh.fetchUser()
            elif choice == "5":
                th.viewTransactions()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    AdminPanel()
