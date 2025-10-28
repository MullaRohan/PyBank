from handeldata.balance_handel import balanceHandel as bh


class UserPanel:
    def __init__(self, user="guest"):
        print("Welcome to the User Panel")
        self.user = user

    def deposit(self):
        bh.deposit(self.user)

    def trasferBal(self):
        # transfer fun will call here
        pass

    def withdraw(self):
        # withdraw fun will call here
        pass

    def checkBalance(self):
        # check balance fun will call here
        pass

    def seeTransaction(self):
        # see transaction fun will call here
        pass

    def changePass(self):
        # change password fun will call here
        pass


if __name__ == "__main__":
    UserPanel()
