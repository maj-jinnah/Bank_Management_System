import random

accounts = []


def find_account(account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None


class User:

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(1000, 9999)
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0
        self.loan_amount = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited {amount} New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount}")
                return f"Withdrew ${amount} New balance: ${self.balance}"
            else:
                return "Withdrawal amount exceeded."
        else:
            return "Invalid withdrawal amount."

    def check_balance(self):
        return f"Available balance: ${self.balance}"

    def get_transaction_history(self):
        return self.transaction_history

    def take_loan(self, loan_amount):
        if self.loan_count < 2:
            if loan_amount > 0:
                self.loan_count += 1
                self.loan_amount += loan_amount
                self.balance += loan_amount
                self.transaction_history.append(
                    f"Took a loan of ${loan_amount}")
                return f"Loan of ${loan_amount} granted."
            else:
                return "Invalid loan amount."
        else:
            return "You have already taken the maximum number of loans."

    def transfer_funds(self, other_account, amount):
        if amount > 0 and self.balance >= amount:
            other_account = find_account(other_account)
            if other_account:
                self.balance -= amount
                other_account.deposit(amount)
                self.transaction_history.append(
                    f"Transferred ${amount} to Account {other_account.account_number}.")
                return f"${amount} transferred to Account {other_account.account_number}."
            else:
                return "Account does not exist."
        else:
            return "Insufficient balance."


class Admin:
    def __init__(self):
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
        account = User(name, email, address, account_type)
        accounts.append(account)
        return f"Congratulation! Your account has been created successfully. Account number is {account.account_number}."

    def delete_account(self, account_number):
        account = find_account(account_number)
        if account:
            accounts.remove(account)
            return "Account successfully deleted."
        else:
            return "This account does not exist."

    def list_accounts(self):
        if accounts:
            for account in accounts:
                print(
                    f"Account Number: {account.account_number}, Name: {account.name}, Email: {account.email}")
        else:
            return "No accounts found."

    def total_available_balance(self):
        total_balance = 0
        for account in accounts:
            total_balance += account.balance
        return f"Total available balance: ${total_balance}"

    def total_loan_amount(self):
        total_loan = 0
        for account in accounts:
            total_loan += (account.loan_amount)
        return f"Total loan: ${total_loan}"

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature
        return "Toggled successfully."


def user_menu():
    while True:
        print("\n::::Banking Management System - User Menu::::\n")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Transaction history")
        print("6. Request a loan")
        print("7. Transfer funds")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings or Current): ")
            account = User(name, email, address, account_type)
            accounts.append(account)
            print(
                f"Congratulation! Your account has been created successfully. Account number is {account.account_number}.")

        if choice == "2":
            account_number = int(input("Enter your account number: "))
            account = find_account(account_number)
            if account:
                amount = float(input("Enter the amount you want to deposit: "))
                print(account.deposit(amount))
            else:
                print("Account not found.")

        elif choice == "3":
            account_number = int(input("Enter your account number: "))
            account = find_account(account_number)
            if account:
                amount = float(
                    input("Enter the amount you want to withdraw: "))
                print(account.withdraw(amount))
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = int(input("Enter your account number: "))
            account = find_account(account_number)
            if account:
                print(account.check_balance())
            else:
                print("Account not found.")

        elif choice == "5":
            account_number = int(input("Enter your account number: "))
            account = find_account(account_number)
            if account:
                history = account.get_transaction_history()
                if history:
                    print("Transaction History:")
                    for transaction in history:
                        print(transaction)
                else:
                    print("No transaction history available.")
            else:
                print("Account not found.")

        elif choice == "6":
            account_number = int(input("Enter your account number: "))
            account = find_account(account_number)
            if account:
                amount = float(input("Enter the loan amount: "))
                print(account.take_loan(amount))
            else:
                print("Account not found.")

        elif choice == "7":
            account_number = int(input("Enter your account number: "))
            account = find_account(account_number)
            if account:
                other_account = int(
                    input("Enter the account number you want to transfer money: "))
                amount = float(
                    input("Enter the amount you want to transfer: "))
                print(account.transfer_funds(other_account, amount))
            else:
                print("Account not found.")

        elif choice == "8":
            break


def admin_menu(admin):
    while True:
        print("\n::::Banking Management System - Admin Menu::::")
        print("1. Create an account")
        print("2. Delete an account")
        print("3. List all accounts")
        print("4. Check total available balance")
        print("5. Check total loan amount")
        print("6. Toggle loan feature")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings or Current): ")
            print(admin.create_account(name, email, address, account_type))

        elif choice == "2":
            account_number = int(input("Enter the account number to delete: "))
            print(admin.delete_account(account_number))

        elif choice == "3":
            admin.list_accounts()

        elif choice == "4":
            print(admin.total_available_balance())

        elif choice == "5":
            print(admin.total_loan_amount())

        elif choice == "6":
            print(admin.toggle_loan_feature())

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


def main():
    admin = Admin()

    while True:
        print("\nBanking Management System")
        print("1. User Menu")
        print("2. Admin Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_menu()

        elif choice == "2":
            admin_menu(admin)

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


main()
