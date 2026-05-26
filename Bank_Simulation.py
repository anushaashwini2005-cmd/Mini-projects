import sqlite3

# DATABASE CONNECTION
try:
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
        id INTEGER PRIMARY KEY,
        holder_name TEXT,
        account_type TEXT,
        balance REAL
    )
    """)

    conn.commit()
    print("Database Connected Successfully")

except sqlite3.Error as e:
    print("Database Error:", e)


# ACCOUNT CLASS
class Account:

    def __init__(self, id, holder_name, balance=0):
        self.id = id
        self.holder_name = holder_name
        self._balance = balance

    def check_balance(self):
        print(f"Available Balance: {self._balance}")

    def deposit(self, amount):

        try:
            if amount <= 0:
                raise ValueError

            self._balance += amount

            cursor.execute(
                "UPDATE accounts SET balance=? WHERE id=?",
                (self._balance, self.id)
            )

            conn.commit()

            print(f"Deposit Successful. Updated Balance: {self._balance}")

        except ValueError:
            print("Enter positive amount only")

    def withdraw(self, amount):

        try:
            if amount <= 0:
                raise ValueError

            if self._balance >= amount:

                self._balance -= amount

                cursor.execute(
                    "UPDATE accounts SET balance=? WHERE id=?",
                    (self._balance, self.id)
                )

                conn.commit()

                print(f"Withdraw Successful. Updated Balance: {self._balance}")

            else:
                print("Insufficient Balance")

        except ValueError:
            print("Enter valid amount")


# SAVINGS ACCOUNT
class SavingsAccount(Account):

    def calculate_interest(self):

        interest_rate = 0.04
        interest = self._balance * interest_rate

        print(f"Interest: {interest}")


# CURRENT ACCOUNT
class CurrentAccount(Account):

    def withdraw(self, amount):

        overdraft_limit = 1000

        try:

            if amount <= 0:
                raise ValueError

            if self._balance - amount >= -overdraft_limit:

                self._balance -= amount

                cursor.execute(
                    "UPDATE accounts SET balance=? WHERE id=?",
                    (self._balance, self.id)
                )

                conn.commit()

                print(f"Withdraw Successful. Updated Balance: {self._balance}")

            else:
                print("Overdraft limit exceeded")

        except ValueError:
            print("Enter valid amount")


# BANK CLASS
class Bank:

    def __init__(self, name, city):

        self.name = name
        self.city = city
        self.__accounts = {}

    def create_account(self, id, holder_name, type):

        try:

            # CHECK IF ID EXISTS
            cursor.execute("SELECT * FROM accounts WHERE id=?", (id,))
            existing = cursor.fetchone()

            if existing:
                print("Account ID already exists")
                return None

            if type == "savings":
                new_account = SavingsAccount(id, holder_name)

            elif type == "current":
                new_account = CurrentAccount(id, holder_name)

            else:
                raise ValueError

            self.__accounts[id] = new_account

            cursor.execute(
                "INSERT INTO accounts VALUES(?,?,?,?)",
                (id, holder_name, type, 0)
            )

            conn.commit()

            print("Account Created Successfully")

            return new_account

        except ValueError:
            print("Invalid account type")

        except sqlite3.Error as e:
            print("Database Error:", e)


banku = Bank("Mysore Bank", "Mysore")


# SAVINGS MENU
def savings(acc):

    while True:

        print("\n1.Deposit")
        print("2.Withdraw")
        print("3.Calculate Interest")
        print("4.Check Balance")
        print("5.Quit")

        choice = input("Enter your choice: ")

        if choice == "1":

            try:
                amt = float(input("Enter amount to deposit: "))
                acc.deposit(amt)

            except ValueError:
                print("Enter numeric value")

        elif choice == "2":

            try:
                draw = float(input("Enter amount to withdraw: "))
                acc.withdraw(draw)

            except ValueError:
                print("Enter numeric value")

        elif choice == "3":
            acc.calculate_interest()

        elif choice == "4":
            acc.check_balance()

        elif choice == "5":
            print("Quitting...")
            break

        else:
            print("Invalid choice")


# CURRENT MENU
def current(acc):

    while True:

        print("\n1.Deposit")
        print("2.Withdraw")
        print("3.Check Balance")
        print("4.Quit")

        choice = input("Enter your choice: ")

        if choice == "1":

            try:
                amt = float(input("Enter amount to deposit: "))
                acc.deposit(amt)

            except ValueError:
                print("Enter numeric value")

        elif choice == "2":

            try:
                draw = float(input("Enter amount to withdraw: "))
                acc.withdraw(draw)

            except ValueError:
                print("Enter numeric value")

        elif choice == "3":
            acc.check_balance()

        elif choice == "4":
            print("Quitting...")
            break

        else:
            print("Invalid choice")


# MAIN PROGRAM
print("Welcome To Mysore Bank")

# ID
while True:

    try:
        Aid = int(input("Enter your id: "))
        break

    except ValueError:
        print("Enter numeric id only")


# HOLDER NAME
while True:

    holder_name = input("Enter holder name: ")

    if holder_name.strip() == "":
        print("Name cannot be empty")

    else:
        break


# ACCOUNT TYPE
while True:

    Atype = input("Enter account type(savings/current): ").lower()

    if Atype in ["savings", "current"]:
        break

    else:
        print("Invalid account type")


acc = banku.create_account(Aid, holder_name, Atype)

if acc:

    if Atype == "savings":
        savings(acc)

    elif Atype == "current":
        current(acc)


# CLOSE DATABASE CONNECTION
conn.close()