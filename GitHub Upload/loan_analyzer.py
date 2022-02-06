# coding: utf-8
import csv
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

# 1. using get() to extract "future value" and "remaining months" data
future_value = loan.get("future_value")
print("The future loan value is $", future_value)

remaining_months = loan.get("remaining_months")
print("The number of remaining months on the loan is", remaining_months)


# 2. Calculate fair value using present value formula
present_value = future_value / (1 + .2/12) ** remaining_months
fair_value = present_value
print("The fair value of the loan is $", (round(fair_value, 2)))

# 3. Conditional statement to decide if the present value represents the loan's fair value
if present_value >= fair_value:
    print("The loan is worth at least the cost to purchase.")
else:
    print("The loan is too expensive and not worth the price.")



"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

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



"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

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

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
