class User:
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance
    def login(self, email, password):
        if self.email == email and self.password == password:
            return True
        else:
            return False
    def update_balance(self, amount):
        self.balance+=amount
        return self.balance
