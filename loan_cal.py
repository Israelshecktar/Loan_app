from tkinter import *
from tkinter import messagebox

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Shecktar Loan Calculator App")
        window.configure(background="lightblue")

        # Initialize input variables
        self.nameVar = StringVar()
        self.currencyOptionVar = StringVar()
        self.loanAmountVar = StringVar()
        self.splitOptionVar = StringVar()
        self.numFriendsVar = StringVar()
        self.interestOptionVar = StringVar()
        self.loanDurationVar = StringVar()
        self.borrowDateVar = StringVar()

        # Create labels and entry fields for the inputs
        Label(window, font='Helvetica 12 bold', text="Name").grid(row=1, column=1, sticky=W)
        self.nameVar = StringVar()
        Entry(window, textvariable=self.nameVar, justify=RIGHT).grid(row=1, column=2)

        Label(window, font='Helvetica 12 bold', text="Currency option (1 for dollars, 2 for naira)").grid(row=2, column=1, sticky=W)
        self.currencyOptionVar = StringVar()
        Entry(window, textvariable=self.currencyOptionVar, justify=RIGHT).grid(row=2, column=2)

        Label(window, font='Helvetica 12 bold', text="Loan amount").grid(row=3, column=1, sticky=W)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)

        Label(window, font='Helvetica 12 bold', text="Split option (1 for alone, 2 for friends)").grid(row=4, column=1, sticky=W)
        self.splitOptionVar = StringVar()
        Entry(window, textvariable=self.splitOptionVar, justify=RIGHT).grid(row=4, column=2)

        Label(window, font='Helvetica 12 bold', text="Number of friends (if splitting)").grid(row=5, column=1, sticky=W)
        self.numFriendsVar = StringVar()
        Entry(window, textvariable=self.numFriendsVar, justify=RIGHT).grid(row=5, column=2)

        Label(window, font='Helvetica 12 bold', text="Interest option (1 for monthly, 2 for yearly)").grid(row=6, column=1, sticky=W)
        self.interestOptionVar = StringVar()
        Entry(window, textvariable=self.interestOptionVar, justify=RIGHT).grid(row=6, column=2)

        Label(window, font='Helvetica 12 bold', text="Loan duration in months").grid(row=7, column=1, sticky=W)
        self.loanDurationVar = StringVar()
        Entry(window, textvariable=self.loanDurationVar, justify=RIGHT).grid(row=7, column=2)

        Label(window, font='Helvetica 12 bold', text="Borrow date (1 for now, 2 for later)").grid(row=8, column=1, sticky=W)
        self.borrowDateVar = StringVar()
        Entry(window, textvariable=self.borrowDateVar, justify=RIGHT).grid(row=8, column=2)

        # Create a button to calculate the loan
        btComputePayment = Button(window, text="Calculate Loan", bg="red", fg="white", font='Helvetica 14 bold', command=self.calculate_loan)
        btComputePayment.grid(row=10, column=2, sticky=E)

        # Create a label to display the results
        self.resultVar = StringVar()
        lblTotalPayment = Label(window, font='Helvetica 12 bold', bg="light green", textvariable=self.resultVar)
        lblTotalPayment.grid(row=11, column=2, sticky=E)

        # Create a button to refresh inputs
        refresh_button = Button(window, text="Refresh Inputs", command=self.refresh_inputs, bg="blue", fg="white", font='Helvetica 14 bold')
        refresh_button.grid(row=12, column=2, pady=10)

        window.mainloop()

    def calculate_loan(self):
        # Validate and process the inputs
        name_value = self.nameVar.get()
        if not name_value.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Name must be a string")
            return

        currency_option_value = self.currencyOptionVar.get()
        if currency_option_value not in ["1", "2"]:
            messagebox.showerror("Error", "Currency option must be 1 or 2")
            return

        loan_amount_value = self.loanAmountVar.get()
        if not loan_amount_value.replace(",", "").replace(".", "").isdigit():
            messagebox.showerror("Error", "Loan amount must be numeric")
            return

        split_option_value = self.splitOptionVar.get()
        if split_option_value not in ["1", "2"]:
            messagebox.showerror("Error", "Split option must be 1 or 2")
            return

        num_friends_value = self.numFriendsVar.get()
        if not num_friends_value.isdigit():
            messagebox.showerror("Error", "Number of friends must be numeric")
            return

        interest_option_value = self.interestOptionVar.get()
        if interest_option_value not in ["1", "2"]:
            messagebox.showerror("Error", "Interest option must be 1 or 2")
            return

        loan_duration_value = self.loanDurationVar.get()
        if not loan_duration_value.isdigit():
            messagebox.showerror("Error", "Loan duration must be numeric")
            return

        borrow_date_value = self.borrowDateVar.get()
        if borrow_date_value not in ["1", "2"]:
            messagebox.showerror("Error", "Borrow date must be 1 or 2")
            return

        currency_symbol = "$" if currency_option_value == "1" else "₦"

        # Set the interest rate
        interest_rate = 0.07 if interest_option_value == "1" else 0.85

        # Calculate the total due payment for the duration
        total_payment = float(loan_amount_value.replace(",", "").replace(".", "")) * (1 + interest_rate * int(loan_duration_value) / 12)

        # Calculate the monthly payment
        monthly_payment = total_payment / int(loan_duration_value)

        # Calculate the payment per person
        payment_per_person = total_payment / int(num_friends_value)

        def refresh_inputs(self):
            self.nameVar.set("")
            self.currencyOptionVar.set("")
            self.loanAmountVar.set("")
            self.splitOptionVar.set("")
            self.numFriendsVar.set("")
            self.interestOptionVar.set("")
            self.loanDurationVar.set("")
            self.borrowDateVar.set("")
            self.resultVar.set("")

        # Format the money with commas
        def format_money(amount):
            amount = f"{amount:.2f}"
            integer, fraction = amount.split(".")
            integer = integer[::-1]
            integer = ",".join([integer[i:i+3] for i in range(0, len(integer), 3)])
            integer = integer[::-1]
            return integer + "." + fraction



        # Set the result
        self.resultVar.set(
            f"The total payment for the loan is {currency_symbol}{format_money(total_payment)}\n"
            f"The monthly payment for the loan is {currency_symbol}{format_money(monthly_payment)}\n"
            f"The payment per person for the loan is {currency_symbol}{format_money(payment_per_person)}"
        )

LoanCalculator()
