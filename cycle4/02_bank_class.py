from random import randint

class BankAccount:
    def __init__(self, acc_no, name, acc_type="savings", balance=0):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
        else:
            print("Not sufficient bank balance")

    def __str__(self):
        line1 = f"Account Number: {self.acc_no}\n"
        line2 = f"Name: {self.name}\n"
        line3 = f"Account type: {self.acc_type}\n"
        line4 = f"Balance: {self.balance}\n"

        return line1 + line2 + line3 + line4

if __name__ == '__main__':
    acc_no = randint(111111111111, 999999999999)
    name = input("Enter name: ")
    acc_type = input("Enter account type: ")

    b1 = BankAccount(acc_no, name, acc_type=acc_type)
    action = input("Enter action(d: Deposit, w: Withdraw, q: Quit): ")
    while (action != 'q'):
        if (action == 'd'):
            b1.deposit(int(input("Enter amount: ")))
        elif action == 'w':
            b1.withdraw(int(input("Enter amount: ")))
        action = input("Enter action(d: Deposit, w: Withdraw, q: Quit): ")
    print()
    print(b1)
