# coding: utf-8
import csv
from multiprocessing.sharedctypes import Value
from pathlib import Path

# Part 1
# loan costs
loan_costs = [500, 600, 200, 1000, 450]

# The total number of loans
total_number_of_loans = (len(loan_costs)) 
print("The total number of loans is",len(loan_costs))

# Total amount of all loans
total_loan_amount = (sum(loan_costs))
print("The total amount of all loans is $",sum(loan_costs))

# Average loan amount
average_loan_amount = total_loan_amount/total_number_of_loans
print("The average loan amount is $",average_loan_amount)




# Part 2
# Loan Data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Usie get() to extract "future value" and "remaining months" data
future_value = loan.get("future_value")
print("The future loan value is $", future_value)

remaining_months = loan.get("remaining_months")
print("The number of remaining months on the loan is", remaining_months)


# Calculate fair value using present value formula
present_value = future_value / (1 + .2/12) ** remaining_months
fair_value = present_value
print("The fair value of the loan is $", (round(fair_value, 2)))

# Conditional statement to decide if the present value represents the loan's fair value
if present_value >= fair_value:
    print("The loan is worth at least the cost to purchase.")
else:
    print("The loan is too expensive and not worth the price.")




# Part 3
# New Loan Data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define function used to calculate present value of new loan
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = (future_value / (1 + annual_discount_rate/12) ** remaining_months)

    return present_value


# Use the function to calculate the present value of the new loan using 0.2 as annual discount rate.
present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate=.2)

print(f"The present value of the loan is: ${present_value: .2f}.")



# Part 4

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# Empty list called "inexpensive_loans"
inexpensive_loans = []


# Loop through loans and append those that are $500 or less into the empty list I created
for item in loans:
    if item.get("loan_price") <= 500:
        inexpensive_loans.append(item)
    

# Print the `inexpensive_loans` list
print("These are the inexpensive loans:", inexpensive_loans)




# Part 5

import csv
from pathlib import Path

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

csvpath = Path("inexpensive_loans.csv")

with open(csvpath, 'w', newline='') as output_file:

    csvwriter = csv.writer(output_file)

    csvwriter.writerow(header)
    
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())


# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
