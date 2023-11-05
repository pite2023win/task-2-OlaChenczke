import logging

def func_name(function):
    def wrapper(*args, **kwargs):
        method_name = function.__name__
        logging.info(f"Using function: {method_name}")
        return function(*args, **kwargs)
    return wrapper

class Client:
    start_balance = 0

    def __init__(self, name, balance=start_balance):
        self.name = name
        self.balance = balance

    @func_name
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            logging.info(f"Deposited ${amount} into {self.name}'s account. New balance: ${self.balance}")
        else:
            logging.error("Invalid deposit amount.")

    @func_name
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            logging.info(f"Withdrew ${amount} from {self.name}'s account. New balance: ${self.balance}")
        else:
            logging.error("Invalid withdrawal amount or insufficient balance.")

    @func_name
    def transfer(self, recipient, amount):
        if amount > 0 and self balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            logging.info(f"Transferred ${amount} from {self.name} to {recipient.name}.")
        else:
            logging.error("Invalid transfer amount or insufficient balance")

    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        self.balance = amount
        logging.info(f"Set balance for {self.name}'s account to ${amount}.")

    def client_data(self):
        return f"Client Name: {self.name}, Balance: ${self.balance}"

    @staticmethod
    @func_name
    def calculate_interest(value, rate, time):
        interest = (value * rate * time) / 100
        logging.info(f"The interest for ${value} at {rate}% for {time} years: {interest}")

class Bank:
    def __init__(self):
        self.clients = []

    def create_client(self, name, initial_balance=0):
        new_client = Client(name, initial_balance)
        self.clients.append(new_client)
        logging.info(f"Created a new client: {name}")

    def get_client(self, name):
        for client in self.clients:
            if client.name == name:
                return client
        return None

    def get_all_clients(self):
        return [client.client_data() for client in self.clients]

    def bank_data(self):
        return f"Total Clients: {len(self.clients)}, Total Balance: ${self.total_balance()}"

    @func_name
    def close_account(self, name):
        for client in self.clients:
            if client.name == name:
                self.clients.remove(client)
                logging.info(f"Closed {name}'s account.")
                return
        logging.error(f"Account for {name} not found.")

    def total_balance(self):
        total = sum(client.balance for client in self.clients)
        return total

    def show_data(self):
        bank_data = self.bank_data()
        list_of_clients = self.get_all_clients()
        logging.info("Bank Details: " + str(bank_data))
        logging.info("All Clients: " + str(list_of_clients))

    @func_name
    def save_clients(self, filename):
        with open(filename, "w") as file:
            for client in self.clients:
                file.write(f"{client.name},{client.balance}\n")
            logging.info("Saved clients' data to " + filename)

    def load_clients(self, filename):
        clients = []
        with open(filename, "r") as file:
            for line in file:
                name, balance = line.strip().split(",")
                client = Client(name, float(balance))
                clients.append(client)
        self.clients = clients
        logging.info("Loaded clients' data from " + filename)

logging.basicConfig(filename='banking_log.txt', level=logging.INFO)

if __name__ == "__main__":
    bank1 = Bank()
    bank2 = Bank()

    bank1.create_client("Scorpion", 1000)
    bank1.create_client("Sub-Zero", 500)
    bank1.create_client("Raiden", 1500)
    #bank2.load_clients("bank2_clients.txt")
    bank2.create_client("Kitana", 2000)
    bank2.create_client("Mileena", 700)

    scorpion = bank1.get_client("Scorpion")
    sub_zero = bank1.get_client("Sub-Zero")
    raiden = bank1.get_client("Raiden")
    kitana = bank2.get_client("Kitana")
    mileena = bank2.get_client("Mileena")

    scorpion.deposit(500)
    scorpion.withdraw(200)
    scorpion.transfer(sub_zero, 300)

    kitana.transfer(mileena, 200)
    mileena.transfer(scorpion, 100)

    raiden.set_balance(2000)
    bank1.close_account("Sub-Zero")

    bank1.save_clients("clients_data_bank1.txt")
    bank2.save_clients("clients_data_bank2.txt")

    bank1.show_data()

    bank2.show_data()

    Client.calculate_interest(2000, 4, 2)
