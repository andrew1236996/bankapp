import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, initial_balance=0, withdrawal_limit=0):
        self.balance = initial_balance
        self.withdrawal_limit = withdrawal_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount and (self.withdrawal_limit == 0 or amount <= self.withdrawal_limit):
            self.balance -= amount
            return True
        else:
            return False

# Create the main application window
window = tk.Tk()
window.title("Banking App")

# Create the account objects
current_account = Account()
savings_account = Account(withdrawal_limit=500)  # Set withdrawal limit for savings account

# Function to handle the deposit button click
def deposit():
    amount = float(deposit_entry.get())
    if account_var.get() == "Current":
        current_account.deposit(amount)
        balance_label.config(text="Current Account Balance: $%.2f" % current_account.balance)
    else:
        savings_account.deposit(amount)
        balance_label.config(text="Savings Account Balance: $%.2f" % savings_account.balance)

# Function to handle the withdraw button click
def withdraw():
    amount = float(withdraw_entry.get())
    if account_var.get() == "Current":
        if current_account.withdraw(amount):
            balance_label.config(text="Current Account Balance: $%.2f" % current_account.balance)
        else:
            balance_label.config(text="Insufficient funds in Current Account")
    else:
        if savings_account.withdraw(amount):
            balance_label.config(text="Savings Account Balance: $%.2f" % savings_account.balance)
        else:
            balance_label.config(text="Insufficient funds in Savings Account")

# Create account selection radio buttons
account_var = tk.StringVar(value="Current")
current_radio = tk.Radiobutton(window, text="Current Account", variable=account_var, value="Current")
savings_radio = tk.Radiobutton(window, text="Savings Account", variable=account_var, value="Savings")
current_radio.pack()
savings_radio.pack()

# Create deposit widgets
deposit_label = tk.Label(window, text="Deposit Amount:")
deposit_entry = tk.Entry(window)
deposit_button = tk.Button(window, text="Deposit", command=deposit)
deposit_label.pack()
deposit_entry.pack()
deposit_button.pack()

# Create withdraw widgets
withdraw_label = tk.Label(window, text="Withdraw Amount:")
withdraw_entry = tk.Entry(window)
withdraw_button = tk.Button(window, text="Withdraw", command=withdraw)
withdraw_label.pack()
withdraw_entry.pack()
withdraw_button.pack()

# Create balance labels
current_balance_label = tk.Label(window, text="Current Account Balance: $%.2f" % current_account.balance)
current_balance_label.pack()
savings_balance_label = tk.Label(window, text="Savings Account Balance: $%.2f" % savings_account.balance)
savings_balance_label.pack()

# Function to handle current account withdrawal
def current_withdrawal():
    amount = float(current_withdraw_entry.get())
    if current_account.withdraw(amount):
        current_balance_label.config(text="Current Account Balance: $%.2f" % current_account.balance)
    else:
        current_balance_label.config(text="Insufficient funds in Current Account")

# Function to handle savings account withdrawal
def savings_withdrawal():
    amount = float(savings_withdraw_entry.get())
    if savings_account.withdraw(amount):
        savings_balance_label.config(text="Savings Account Balance: $%.2f" % savings_account.balance)
    else:
        savings_balance_label.config(text="Insufficient funds in Savings Account")

# Create current account withdrawal widgets
current_withdraw_label = tk.Label(window, text="Current Account Withdrawal:")
current_withdraw_entry = tk.Entry(window)
current_withdraw_button = tk.Button(window, text="Withdraw", command=current_withdrawal)
current_withdraw_label.pack()
current_withdraw_entry.pack()
current_withdraw_button.pack()

# Create savings account withdrawal widgets
savings_withdraw_label = tk.Label(window, text="Savings Account Withdrawal:")
savings_withdraw_entry = tk.Entry(window)
savings_withdraw_button = tk.Button(window, text="Withdraw", command=savings_withdrawal)
savings_withdraw_label.pack()
savings_withdraw_entry.pack()
savings_withdraw_button.pack()

# Function to handle current account deposit
def current_deposit():
    amount = float(current_deposit_entry.get())
    current_account.deposit(amount)
    current_balance_label.config(text="Current Account Balance: $%.2f" % current_account.balance)

# Function to handle savings account deposit
def savings_deposit():
    amount = float(savings_deposit_entry.get())
    savings_account.deposit(amount)
    savings_balance_label.config(text="Savings Account Balance: $%.2f" % savings_account.balance)

# Create current account deposit widgets
current_deposit_label = tk.Label(window, text="Current Account Deposit:")
current_deposit_entry = tk.Entry(window)
current_deposit_button = tk.Button(window, text="Deposit", command=current_deposit)
current_deposit_label.pack()
current_deposit_entry.pack()
current_deposit_button.pack()

# Create savings account deposit widgets
savings_deposit_label = tk.Label(window, text="Savings Account Deposit:")
savings_deposit_entry = tk.Entry(window)
savings_deposit_button = tk.Button(window, text="Deposit", command=savings_deposit)
savings_deposit_label.pack()
savings_deposit_entry.pack()
savings_deposit_button.pack()

# Run the main window event loop
window.mainloop()