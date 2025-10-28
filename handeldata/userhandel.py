import pandas as pd

user_df = pd.read_csv("data/user.csv")


class Userhandel:
    def __init__(self):
        self.user = self

    def addUser(self):
        name = input("Enter name: ")
        user_name = input("Enter username: ")
        if user_name in user_df["user_name"].values:
            print("-> User already exists. Try another username.")
            return
        password = input("Enter password: ")
        amount = float(input("Enter initial amount: "))
        limit = float(input("Enter transaction limit: "))
        new_user = {
            "name": name,
            "user_name": user_name,
            "password": password,
            "amount": amount,
            "limit": limit,
        }
        user_df.loc[len(user_df)] = new_user
        user_df.to_csv("data/user.csv", index=False)
        print(f"-> User {user_name} added successfully.")

    def deleteUser(self):
        user = input("Enter username to delete: ").strip()
        matched_rows = user_df[user_df["user_name"] == user]
        if not matched_rows.empty:
            user_df.drop(matched_rows.index, inplace=True)
            user_df.to_csv("data/user.csv", index=False)
            print(f"-> User {user} deleted successfully.")
            return
        else:
            print("-> User not found.")
            return

    def fetchUser(self):
        user = input("Enter username for full details: ").strip()
        matched_rows = user_df[user_df["user_name"] == user]
        if not matched_rows.empty:
            print(
                matched_rows.drop(columns=["password", "user_name"]).to_string(
                    index=False
                )
            )
            return
        else:
            print("-> User not found.")
            return


if __name__ == "__main__":
    uh = Userhandel()
    # uh.addUser()
    # uh.fetchUser()
