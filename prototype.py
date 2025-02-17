MAX_LOAN_AMOUNT = 10_000
INTEREST_RATE = 0.03

class Bank:
    def __init__(self, first_name, last_name, account_pass):

        self.__account_holders = first_name + last_name
        self.__account_pass = account_pass

        self.__history = []

        self.__loans_history = []
        self.__total_loan = 0


        self.__accounts_and_balance = {}
        self.__accounts_iterator = 0




    @staticmethod
    def display_menu():
        """Main menu for banking system."""
        print("\n🌟 Welcome to Enhanced Bank System 🌟")
        print("1️⃣ Create Account")
        print("2️⃣ Close Account")
        print("3️⃣ Deposit Money")
        print("4️⃣ Withdraw Money")
        print("5️⃣ Check Balance")
        print("6️⃣ List All Accounts")
        print("7️⃣ Transfer Funds NOT AVAILABLE")
        print("8️⃣ View Transaction History")
        # print("9️⃣ Apply for Loan")
        # print("🔟 Repay Loan")
        # print("1️⃣1️⃣ Identify Credit Card Type")
        print("0️⃣ Exit")

    def password_checker(self, input_password):
        if int(input_password) == self.__account_pass:
            return True
        else:
            return False

    def create_account(self, input_currency, total_accounts = 0):
        if total_accounts >= 5:
            return "You have reached the limit for currency account"

        else:
            self.__accounts_and_balance[input_currency] = 0
            self.__accounts_iterator += 1
            self.__history.append(f"Crated an account with currency {input_currency}")

            return f"✅ Successfully added an account. Accounts left to make: {5 - self.__accounts_iterator}"


    def close_account(self, close_currency, transfer_funds_to):
        self.__accounts_and_balance[transfer_funds_to] += self.__accounts_and_balance[close_currency]
        del self.__accounts_and_balance[close_currency]
        self.__history.append(f"Closed an account {close_currency}, money from the account have"
                              f"been transfered to {transfer_funds_to}")
        return f"✅ Successfully removed an account currency! Total active current accounts: {self.__accounts_and_balance.keys()}"


    def deposit(self, amount, currency_input):
        self.__accounts_and_balance[currency_input] += amount
        self.__history.append(f"Deposited {amount} in {currency}.")

        return f"✅ Successfully added {amount} to {currency_input}!"


    def withdraw(self, amount, currency_input):
        self.__accounts_and_balance[currency_input] -= amount
        self.__history.append(f"Withdraw {amount} in {currency}.")
        return f"✅ Successfully withdraw {amount} from {currency_input}, amount left: {self.__accounts_and_balance[currency_input]} "


    def check_balance(self, currency_input):
        return f"✅ {currency_input} : {self.__accounts_and_balance.get(currency_input)}"

    def list_accounts(self):
        if self.__accounts_and_balance:
            for value in self.__accounts_and_balance.values():
                for key in self.__accounts_and_balance.keys():
                    print(f"💲{value} : {key}")

        else:
            print(f"You don't have any accounts!")


    def transfer_funds(self, transfer_from_account, transfer_to_account):
        pass


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





bank_instance = Bank("Ivan", "Ivanov", 123)

password = input("Enter your password to continue using the application: ")
if bank_instance.password_checker(password):

    while True:
            bank_instance.display_menu()
            choice = int(input("Enter your choice: "))


            if choice == 1:
                currency = input("Input what currency you would like to use: ")
                print(bank_instance.create_account(currency))
                print()

            elif choice == 2:
                currency = input("Input what currency you would like to remove: ")
                transfer_money_to = input("Where you want to transfer money to: ")
                print(bank_instance.close_account(currency,transfer_money_to))

            elif choice == 3:
                currency = input("Input what currency you would like to deposit to: ")
                money_deposit = float(input("Enter the amount you want to deposit: "))
                print(bank_instance.deposit(money_deposit, currency))

            elif choice == 4:
                currency = input("Input from which currency you would like to withdraw: ")
                money_deposit = float(input("Enter the amount you want to withdraw: "))
                print(bank_instance.withdraw(money_deposit, currency))

            elif choice == 5:
                currency = input("Input from which currency you would like to get information: ")
                print(bank_instance.check_balance(currency))

            elif choice == 6:
                print(bank_instance.list_accounts())

            elif choice == 7:
                print("There is a transfer fee of 3% per transfer!")
                transfer_from_currency = input("Enter a currency from which you want to transfer.")
                transfer_to_currency = input("Enter a currency to which the money transfer.")
                print(bank_instance.transfer_funds())

            elif choice == 8:
                print(bank_instance.view_transaction_history())

            # elif choice == 9:
            #     apply_for_loan()
            # elif choice == 10:
            #     repay_loan()
            # elif choice == 11:
            #     identify_card_type()

            elif choice == 0:
                print("Goodbye! 👋")
                break
            else:
                print("❌ Invalid choice. Try again!")

