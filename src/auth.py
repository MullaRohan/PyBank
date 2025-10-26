import pandas as pd
from src import admin_panel
from src import user_panel

# loading admin and user data from csv files
admin_df = pd.read_csv("data/admin.csv", dtype={"password": str})
user_df = pd.read_csv("data/user.csv", dtype={"password": str})


class Auth:
    # input user and password from main.py
    def __init__(self, user, password):
        self.user = user
        self.passw = password
        self.userChecking()

    # checking and redirecting user to respective panel
    def userChecking(self):
        user_identity = 0
        if (
            self.user in admin_df["user_name"].values
            and self.passw in admin_df["password"].values
        ):
            user_identity = 1
        elif (
            self.user in user_df["user_name"].values
            and self.passw in user_df["password"].values
        ):
            user_identity = 2

        # validating user identity and redirecting to respective panel
        if user_identity == 1:
            admin_panel.AdminPanel()
        elif user_identity == 2:
            user_panel.UserPanel()
        # user not found exiting program to main.py
        else:
            print("Not Found")
            exit()
