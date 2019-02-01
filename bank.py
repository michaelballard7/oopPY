
class Account:

    def __init__(self, filepath):
        self.filepath = 'balance.txt'
        self.pin = input("Please enter the client pin: ")
        self.client_pin = 1984
        self.signed_in = False
        # self.leverage_access = true
        with open(self.filepath, 'r') as file:
            self.initial = int(file.read())
        self.balance = self.initial

    def generate_credentials(self):
        pass

    def validate(self):
        if int(self.pin) == self.client_pin:
            self.signed_in = True
            return True

    def withdraw(self, amount):
        print("account value before withdraw is:", self.balance)
        if self.validate():
            if self.balance > amount:
                self.balance = self.balance - amount
                print("From in withdraw balance is", self.balance)
                self.save_balance(self.balance)
        else:
            return "insufficient funds"

    def deposit(self, amount):
        if self.signed_in:
            self.balance = self.balance + amount
        elif self.validate():
            self.balance = self.balance + amount
        else:
            return "Invalid account"
        return "Your new balance is {}".format(self.get_balance())

    def get_balance(self):
        return self.balance

    def save_balance(self, new_balance):
        with open(self.filepath, 'w') as file:
            file.write(str(int(new_balance)))
        print("balance after save is :", self.balance)

    def transfer_balance(self, amount):
        pass


class Leverage_Account(Account):

    def __init__(self):
        pass


# checking = Account('balance.txt')
# print(checking.withdraw(300))
# print(checking.deposit(300000))
# checking.save_balance()
