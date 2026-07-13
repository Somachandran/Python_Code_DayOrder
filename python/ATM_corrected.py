# ATM System


class Interger(Exception):
    pass


class bank_account:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self):
        try:
            amount = int(input("Enter the Amount: "))
            if amount <= 0:
                raise Interger("Enter a valid amount (> 0)")
            self.balance += amount
            print("Amount Deposited Successfully.")
            print("Current Balance : ", self.balance)
        except Interger as e:
            print(e)
        except ValueError:
            print("please enter only numeric values")

    def withdraw(self):
        try:
            withdraw_amt = int(input("Enter Withdraw Amount: "))
            if withdraw_amt <= 0:
                raise Interger("Enter a valid withdraw amount (> 0)")
            if withdraw_amt <= self.balance:
                self.balance -= withdraw_amt
                print("Current Balance: ", self.balance)
            else:
                print("Insufficient Balance")
        except Interger as e:
            print(e)
        except ValueError:
            print("please enter only numeric values")

    def check_balance(self):
        print("Your Balance: ", self.balance)


class savings_acc(bank_account):
    def interest_rate(self):
        try:
            inter = int(input("Enter Interest percentage: "))
            if not 10 <= inter <= 100:
                raise Interger("Enter only number 10 to 100")
            interest = (inter / 100) * self.balance
            self.balance += interest
            print("New Balance: ", self.balance)
        except Interger as e:
            print(e)
        except ValueError:
            print("please enter only numeric values")


class current_acc(bank_account):
    overdraft_limit = 500

    def withdraw(self):
        try:
            amt = int(input("Enter amount : "))
            if amt <= 0:
                raise Interger("Enter a valid amount (> 0)")

            if amt <= self.balance + self.overdraft_limit:
                self.balance -= amt
                print("Current Balance: ", self.balance)
            else:
                print("Overdraft Limit Exceeded")
        except Interger as e:
            print(e)
        except ValueError:
            print("please enter only numeric values")


obj = bank_account(123456, "sriram", 100000)
obj1 = savings_acc(123456, "sriram", 100000)

text = ("======ATM====")
print(text.center(40))
print(
    """
1.Deposit
2.Withdraw
3.Check Balance
4.Add Interest
5.Exit
      """
)

while True:
    try:
        i = int(input("Enter your choice: "))
    except ValueError:
        print("please enter only numeric values")
        continue

    if i == 1:
        obj.deposit()
    elif i == 2:
        obj.withdraw()
    elif i == 3:
        obj.check_balance()
    elif i == 4:
        obj1.interest_rate()
    elif i == 5:
        print("Thank You For Using ATM")
        break
    else:
        print("Invalid choice")

