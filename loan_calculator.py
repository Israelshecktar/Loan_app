# print a statement welcome the user to my loan calculator app
print("Welcome to shecktar loan calculator app!")
print("")

# Ask for the users name and greet the user
name = input("What is your name? ")
print(f"Hello, {name}!")
print("")

# Ask if the user will like to borrow in dollars or naira
currency_option = input("Would you like to borrow in dollars or naira? (1 for dollars, 2 for naira) ")
print("")

# validate the input
while currency_option not in ["1", "2"]:
    print("Please enter a valid response.")
    currency_option = input("Would you like to borrow in dollars or naira? (1 for dollars, 2 for naira) ")
    print("")

# set the currency symbol
if currency_option == "1":
    currency_symbol = "$"
else:
    currency_symbol = "₦"

# Ask the user how much they would like to borrow
loan_amount = input(f"How much would you like to borrow in {currency_symbol}? ")
print("")

# validate the input
while not loan_amount.replace(",", "").isnumeric():
    print("Invalid amount. Please enter a valid amount.")
    loan_amount = input(f"How much would you like to borrow in {currency_symbol}? ")
    print("")

# convert the input to a float and remove the commas
loan_amount = float(loan_amount.replace(",", ""))

# Ask if the user would like to borrow the loan alone or split the loan with some friends
split_option = input("Would you like to borrow the loan alone or split the loan with some friends? (1 for alone, 2 for friends) ")
print("")

# validate the input
while split_option not in ["1", "2"]:
    print("Please enter a valid response.")
    split_option = input("Would you like to borrow the loan alone or split the loan with some friends? (1 for alone, 2 for friends) ")
    print("")

# Ask the user how many people to split the loan bill with
if split_option == "2":
    num_friends = input("How many people to split the loan bill with? ")
    print("")
    # validate the input
    while not num_friends.isnumeric():
        print("Invalid number. Please enter a valid number.")
        num_friends = input("How many people to split the loan bill with? ")
        print("")
    # convert the input to an int
    num_friends = int(num_friends)
else:
    num_friends = 1

# inform the user of the interest rates
print("The interest rates for the loan are as follows:")
print("For monthly interest, it is 7% interest rate")
print("For yearly interest, it is 85% interest rate")
print("")

# Ask the user to choose between monthly interest or yearly interest
interest_option = input("Would you like to pay monthly interest or yearly interest? (1 for monthly, 2 for yearly) ")
print("")

# validate the input
while interest_option not in ["1", "2"]:
    print("Please enter a valid response.")
    interest_option = input("Would you like to pay monthly interest or yearly interest? (1 for monthly, 2 for yearly) ")
    print("")

# for monthly interest it is 7% interest rate
if interest_option == "1":
    interest_rate = 0.07
# for yearly interest it is 85% interest rate
else:
    interest_rate = 0.85

# Ask the user for the duration they'd like to borrow the loan for
loan_duration = input("How long would you like to borrow the loan for in months? The maximum duration is 5 years, which is 60 months. ")
print("")

# validate the input
while not loan_duration.isnumeric() or int(loan_duration) > 60:
    print("Invalid number. Please enter a valid number within the range.")
    loan_duration = input("How long would you like to borrow the loan for in months? The maximum duration is 5 years, which is 60 months. ")
    print("")

# convert the input to an int
loan_duration = int(loan_duration)

# calculate the total due payment for the duration
total_payment = loan_amount * (1 + interest_rate * loan_duration / 12)

# calculate the monthly payment
monthly_payment = total_payment / loan_duration

# calculate the payment per person
payment_per_person = total_payment / num_friends

# define a function to format the money with commas
def format_money(amount):
    # convert the amount to a string with two decimal places
    amount = f"{amount:.2f}"
    # split the amount into the integer and fractional parts
    integer, fraction = amount.split(".")
    # reverse the integer part
    integer = integer[::-1]
    # insert a comma after every three digits
    integer = ",".join([integer[i:i+3] for i in range(0, len(integer), 3)])
    # reverse the integer part back
    integer = integer[::-1]
    # return the formatted amount
    return integer + "." + fraction

# print the results
print(f"The total payment for the loan is {currency_symbol}{format_money(total_payment)}")
print(f"The monthly payment for the loan is {currency_symbol}{format_money(monthly_payment)}")
if num_friends > 1:
    print(f"The payment per person for the loan is {currency_symbol}{format_money(payment_per_person)}")
print("")

# Ask the user what date they would like to borrow the loan
borrow_date = input("What date would you like to borrow the loan? (1 for now, 2 for later) ")
print("")

# validate the input
while borrow_date not in ["1", "2"]:
    print("Please enter a valid response.")
    borrow_date = input("What date would you like to borrow the loan? (1 for now, 2 for later) ")
    print("")

# import the datetime module
import datetime

# get the current date
today = datetime.date.today()

# if now, return the payment due date
if borrow_date == "1":
    # calculate the payment due date by adding the loan duration to the current date
    due_date = today + datetime.timedelta(days=loan_duration * 30)
    # change the payment due date format to dd-mm-yyyy
    due_date = due_date.strftime("%d-%m-%Y")
    print(f"The payment due date is {due_date}")
    print("")
# if later, calculate the payment due date
else:
    # ask the user for the date they want to borrow the loan
    borrow_date = input("Please enter the date you want to borrow the loan in dd-mm-yyyy format: ")
    print("")
    # validate the input
    while True:
        try:
            # convert the input to a date object
            borrow_date = datetime.datetime.strptime(borrow_date, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Invalid date. Please enter a valid date.")
            borrow_date = input("Please enter the date you want to borrow the loan in dd-mm-yyyy format: ")
            print("")
    # calculate the payment due date by adding the loan duration to the borrow date
    due_date = borrow_date + datetime.timedelta(days=loan_duration * 30)
    # change the payment due date format to dd-mm-yyyy
    due_date = due_date.strftime("%d-%m-%Y")
    print(f"The payment due date is {due_date}")
    print("")

# Ask the user if that would be all for now
answer = input("Would that be all for now? (1 for yes, 2 for no) ")
print("")

# validate the input
while answer not in ["1", "2"]:
    print("Please enter a valid response.")
    answer = input("Would that be all for now? (1 for yes, 2 for no) ")
    print("")

# if yes, thank the user and exit the app
if answer == "1":
    print(f"Thank you for using my loan calculator app, {name}! Have a nice day!")
    print("")
# if no, ask the user what they would like to do or otherwise transfer them to a customer care representative
else:
    print(f"What else would you like to do, {name}? If you need more help, please contact our customer care representative at 0903-377-3871.")
    print("")
