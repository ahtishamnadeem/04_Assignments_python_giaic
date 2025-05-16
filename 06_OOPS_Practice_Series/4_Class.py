class Bank:
    bank_name = "Royal Bank"  # Class variable

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Changing class variable for all instances

    def display(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")

# Example usage:
cust1 = Bank("Amna")
cust2 = Bank("Zara")

cust1.display()
cust2.display()

# Change bank name
Bank.change_bank_name("Women's Bank")

cust1.display()
cust2.display()
