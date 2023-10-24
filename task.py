class Bank:

    clients={}

class Client:

    def __init__(self, client_name, balance):
        self.client_name = client_name
        self.balance = balance

    def cash_input(self, add_money):
        self.add_money = add_money
        add_money = input("How much money would you like to input?: ")
        self.balance += add_money
        print(f"Your balance is: {self.balance}")

    def cash_withdrawal(self, subtract_money):
        self.subtract_money = subtract_money
        subtract_money = input("How much money would you like to withdrawal?: ")
        self.balance -= subtract_money
        print(f"Your balance is: {self.balance}")

client1 = Client("Jan Kowalski", 1200)
client2 = Client("Mariusz Pudzianowski", 1600)
