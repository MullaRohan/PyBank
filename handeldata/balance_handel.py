import pandas as pd
import datetime
import random
import string

transCS = pd.read_csv("data/transactions.csv")
userCS = pd.read_csv("data/user.csv", dtype={"password": str})


def generate_transaction_id():
    chars = string.ascii_uppercase + string.digits
    transaction_id = "".join(random.choices(chars, k=8))
    return transaction_id


def generate_timestamp():
    return f"{datetime.datetime.now().strftime('%d-%m-%Y at %H:%M')}"


transCSV = pd.DataFrame(transCS)
userCSV = pd.DataFrame(userCS)


class balanceHandel:
    def __init__(self):
        pass

    def deposit(self, username):
        # deposit function
        print(f"Deposit for user: {username}")
        amnt = float(input("Enter amount to deposit: "))
        userCSV.loc[userCSV["user_name"] == username.strip(), "amount"] += amnt
        userCSV.to_csv("data/user.csv", index=False)
        print("Deposit successful.")
        # transaction and log funciton
        new_transaction = {
            "user_name": username,
            "amount": amnt,
            "type": "deposit",
            "transaction_id": generate_transaction_id(),
            "date": generate_timestamp(),
        }
        global transCSV
        transCSV = pd.concat(
            [transCSV, pd.DataFrame([new_transaction])], ignore_index=True
        )
        transCSV.to_csv("data/transactions.csv", index=False)
        print("Transaction Created.")


if __name__ == "__main__":
    balanceHandel().deposit("roton")
    # print(generate_timestamp())
