# In this Python program, the user inputs what they would like to calculate (interest on their investment or monthly
# home loan repayments).
# The user then inputs the required information for the specified calculator.
# The program then outputs the users interest on investment, or their monthly home loan repayment amount based on
# their selection.

import math

print("Investment - Calculate the amount of interest you will earn on your investment."
      "\nBond - Calculate the amount you will have to pay on a home loan.")

user_selection = input("\nEnter either 'Investment' or 'Bond' to continue: ")

# User inputs variables for investment interest calculations
if user_selection.lower() == "investment":
    deposit = round(float(input("Enter the value of your deposit: ")), 2)
    investment_interest_rate = round(float(input("What is the interest rate e.g. '8' = 8%: ")) / 100, 2)
    investment_length = int(input("How many years do you plan to have this investment: "))
    interest_type = input("\nSimple Interest - Interest calculated on the initial amount of the investment."
                          "\nCompound Interest - Interest is calculated on the accumulated amount of the investment."
                          "\n\nEnter the type of interest you will receive, 'Simple' or 'Compound': ")

    # Outputs the calculation of either the simple or compound interest
    if interest_type.lower() == "simple":
        total_simple_interest = round(deposit * (1 + (investment_interest_rate) * investment_length), 2)
        print(f"\nThe total amount of your investment after {investment_length} years will be "
              f"£{total_simple_interest}.")
    if interest_type.lower() == "compound":
        total_compound_interest = round(deposit * math.pow((1 + investment_interest_rate), investment_length), 2)
        print(f"\nThe total amount of your investment after {investment_length} years will be "
              f"£{total_compound_interest}.")

# User inputs variables for house loan repayments
elif user_selection.lower() == "bond":
    house_value = round(float(input("Enter the current value of the house: ")), 2)
    bond_interest_rate = round(float(input("Enter the interest rate of the loan e.g. '8' = 8%: ")) / 100, 2)
    repayment_term = int(input("Enter the number of months you plan to repay the bond: "))
    monthly_loan_repayment = round(((bond_interest_rate / 12) * house_value) /
                                   (1 - ((1 + (bond_interest_rate / 12)) ** (-repayment_term))), 2)

    # Outputs calculation of monthly repayment amount
    print(f"\nThe amount to be paid monthly on your house loan is £{monthly_loan_repayment} for a "
          f"period of {repayment_term} months.")
else:
    print("\nInvalid entry.")