MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03

class Bank:
    def __init__(self, first_name, last_name, account_pass):

        self.__account_holders = first_name + last_name
        self.__account_pass = account_pass

        self.__balances = {}

        self.__accounts = []
        self.__accounts_iterator = 0

        self.__history = []

        self.__loans = []

        self.__total_loan_num = 0

        self.__bgn_balance = 0
        self.__usd_balance = 0
        self.__cad_balance = 0
        self.__try_balance = 0
        self.__gbp_balance = 0
        self.__available_accounts = ["BGN", "USD", "CAD", "TRY", "GBP"]

    @staticmethod
    def display_menu():
        """Main menu for banking system."""
        print("\n🌟 Welcome to Enhanced Bank System 🌟")
        print("1️⃣ Create Account")
        print("2️⃣ Deposit Money")
        print("3️⃣ Withdraw Money")
        print("4️⃣ Check Balance")
        print("5️⃣ List All Accounts")
        print("6️⃣ Transfer Funds")
        print("7️⃣ View Transaction History")
        print("8️⃣ Apply for Loan")
        print("9️⃣ Repay Loan")
        print("🔟 Identify Credit Card Type")
        print("0️⃣ Exit")


    def create_account(self, input_currency, password, total_accounts = 0):
        if input_currency in self.__available_accounts:


            if total_accounts >= 5:
                return "You have reached the limit for currency account"

            else:
                if password == self.__account_pass:
                    self.__accounts.append(f"{self.__accounts_iterator} - {input_currency}")
                    self.__accounts_iterator += 1

                    return f"Successfully added an account."
                else:
                    return f"Incorrect password!"

        else:
            return "Invalid currency. Available currencies are BGN, USD, CAD, TRY and GBP"

    def close_account(self, close_currency, password):
        if password == self.__account_pass:
            self.__accounts.remove(close_currency)
            return f"Successfully removed an account currency! Total active current accounts: {len(self.__accounts)}"
        else:
            return f"Incorrect password!"



    def deposit(self, amount, password, currency):
        if password == self.__account_pass:
            if currency == "BGN":
                self.__bgn_balance += amount
                return f"Added {amount} to your BGN currency account."

            elif currency == "USD":
                self.__usd_balance += amount
                return f"Added {amount} to your USD currency account."

            elif currency == "CAD":
                self.__cad_balance += amount
                return f"Added {amount} to your CAD currency account."

            elif currency == "TRY":
                self.__try_balance += amount
                return f"Added {amount} to your TRY currency account."

            elif currency == "GBP":
                self.__gbp_balance += amount
                return f"Added {amount} to your GBP currency account."


            self.__history.append(f"Deposited {amount} in {currency}.")



        else:
            return "Invalid password!"


    def withdraw(self, amount, password, currency):
        if password == self.__account_pass:
            if currency == "BGN":
                self.__bgn_balance -= amount
                return f"Withdraw {amount} from your BGN currency account."

            elif currency == "USD":
                self.__usd_balance -= amount
                return f"Withdraw {amount} from your USD currency account."

            elif currency == "CAD":
                self.__cad_balance -= amount
                return f"Withdraw {amount} from your CAD currency account."

            elif currency == "TRY":
                self.__try_balance -= amount
                return f"Withdraw {amount} from your TRY currency account."

            elif currency == "GBP":
                self.__gbp_balance -= amount
                return f"Withdraw {amount} from your GBP currency account."


            self.__history.append(f"Withdraw {amount} in {currency}.")

        else:
            return "Invalid password!"



    def check_balance(self, currency, password):
        if password == self.__account_pass:
            if currency == "BGN":
                return self.__bgn_balance
            elif currency == "USD":
                return self.__usd_balance
            elif currency == "CAD":
                return self.__cad_balance
            elif currency == "TRY":
                return self.__try_balance
            elif currency == "GBP":
                return self.__gbp_balance

        else:
            return "Invalid password!"


    def list_accounts(self):
        for account in self.__accounts:
            if account == "BGN":
                print(f"BGN: {self.__bgn_balance}")
            elif account == "USD":
                print(f"USD: {self.__usd_balance}")
            elif account == "CAD":
                print(f"CAD: {self.__cad_balance}")
            elif account == "TRY":
                print(f"TRY: {self.__try_balance}")
            elif account == "GBP":
                print(f"GBP: {self.__gbp_balance}")


    #use api
    # def transfer_funds():
    #     """Transfer funds between two accounts."""
    #     pass

    def view_transaction_history(self):
        return "".join(self.__history)

    # def apply_for_loan():
    #
    # def repay_loan():
    #     """Allow user to repay a loan."""
    #     pass
    #
    # def identify_card_type():
    #     """Identify type of credit card."""
    #     pass





bank_instance = Bank("Baby", "Gril", 123)



while True:
    bank_instance.display_menu()
    choice = int(input("Enter your choice: "))
    # Map choices to functions
    if choice == 1:
        currency = input("Input what currency you would like to use: ")
        pass_input = int(input("Enter your password: "))
        print(bank_instance.create_account(currency, pass_input))

    elif choice == 2:
        money_deposit = float(input("Enter the amount you want to deposit: "))
        pass_input = int(input("Enter your password: "))
        currency = input("Input what currency you would like to deposit to: ")
        print(bank_instance.deposit(money_deposit, pass_input, currency))

    # elif choice == 2:
    #     currency = input("Input what currency you would like to remove: ")
    #     pass_input = int(input("Enter your password: "))
    #     bank_instance.close_account(currency, pass_input)

    elif choice == 3:
        money_deposit = float(input("Enter the amount you want to deposit: "))
        pass_input = int(input("Enter your password: "))
        currency = input("Input from which currency you would like to withdraw: ")
        print(bank_instance.withdraw(money_deposit, pass_input, currency))

    elif choice == 4:
        currency = input("Input from which currency you would like to get information: ")
        pass_input = int(input("Enter your password: "))
        print(bank_instance.check_balance(currency, pass_input))

    elif choice == 5:
        print(bank_instance.list_accounts())
    # elif choice == 6:
    #     transfer_funds()
    elif choice == 7:
        print(bank_instance.view_transaction_history())

    # elif choice == 8:
    #     apply_for_loan()
    # elif choice == 9:
    #     repay_loan()
    # elif choice == 10:
    #     identify_card_type()

    elif choice == 0:
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice. Try again!")

