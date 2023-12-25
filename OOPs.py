"""functions and methods are different. Methods are functions written within a class. 
A class is a template for objects and an object is an instance of a class."""

"""init is a magic method that is a constructor. Magic methods are methods that an object cannot call. """

class Atm:
    def __init__(self):
        self.pin = ""  # Initialize pin as an empty string
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""Hello, how would you like to proceed?
                           1. Enter 1 to create pin.
                           2. Enter 2 to deposit.
                           3. Enter 3 to withdraw.
                           4. Enter 4 to check balance.
                           5. Enter 5 to exit.
                           Please enter your choice:    """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            pass
        


    def create_pin(self):
        self.pin = input("Enter your new pin: ")
        print("Pin set successfully.")

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid Pin.")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds. Your available balance is:", self.balance)
        else:
            print("Invalid Pin.")


# Create an instance of the Atm class
sbi = Atm()
sbi.menu()


class Fraction:
    """Class that allows users to do operations in fractions instead of decimals. """
    def __init__(self,n,d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        temp_num = self.num*self.den + other.num*self.den
        temp_den = self.den*other.den
        return "{}/{}".format(temp.num,temp.den)
    def __sub__(self,other):
        temp_num = self.num*self.den - other.num*self.den
        temp_den = self.den*other.den
        return "{}/{}".format(temp.num,self.den)
    def __mul__(self,other):
        temp_num = self.num*other_den + self.den*other_num



