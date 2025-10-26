# import time
from src import auth


def main():
    user_name = input("1️⃣ Enter Your User Name: ")
    password = input("2️⃣ Enter Your Password: ")

    print("\nPlease wait while checking the info ")
    auth.Auth(user_name, password)


if __name__ == "__main__":
    main()
