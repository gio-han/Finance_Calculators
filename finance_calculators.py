'''
PSEUDO CODE
Import the math module
Display the menu options i.e. investment or bond calculation
Allow user to choose option and account for different capitalisations
1) Accesss to investment calculator
    Nested statements for types of interest: simple or compound
    Calculate and display the approprite amount user will get back
2) Access to home loan repayment calculator
    Calculate and display amount user will have to repay each month
3) Error message if invalid input entered
'''

# FINANCE CALCULATORS
# The program below allows the user to access two different calculators :
# An investment calculator and home loan repayment

import math

while True:
    print("""
*** FINANCE CALCULATORS ***
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan""")

    calculation_type = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    # Accesses the investment calculator
    if calculation_type == "investment":
    
        try:
            # Takes and converts all the required details from user
            money_amount = float(input("\nEnter the amount of money that you are depositing: "))
            annual_rate = float(input("\nEnter the annual interest rate as a percentage without the '%' sign: "))
            dec_annual_rate = annual_rate / 100
            planned_years = float(input("\nEnter the number of years you plan on investing: "))
            interest = str(input("\nEnter either 'simple' or 'compound' to select the corresponding type of interest: ").lower())

        except ValueError:
            print("\n!!! Invalid input - Please enter a number")
            continue

        # Nested if statement accesses the simple interest investment calculator, does all the calculations and prints the outputs
        if interest == "simple":
            tot_with_simple_interest = money_amount * (1 + dec_annual_rate * planned_years)
            rounded_tot_with_simple = round(tot_with_simple_interest, 2)
            print(f"\nThe total amount you'll get back after {planned_years} year(s), at a {annual_rate}% {interest} interest rate is: {rounded_tot_with_simple}")
            gross_profit_simple = round((rounded_tot_with_simple - money_amount), 2)
            print(f"Taking your initial investment of {money_amount} into account, that means you'll make a gross profit of: {gross_profit_simple}\n")
            continue

        # Nested elif statement accesses the compound interest investment calculator, does all the calculations and prints the outputs
        elif interest == "compound":
            tot_with_compound_interest = money_amount * math.pow((1 + dec_annual_rate), planned_years)
            rounded_tot_with_compound = round(tot_with_compound_interest, 2)
            print(f"\nThe total amount you'll get back after {planned_years} year(s), at a {annual_rate}% {interest} interest rate is: {rounded_tot_with_compound}")
            gross_profit_compound = round((rounded_tot_with_compound - money_amount), 2)
            print(f"Taking your initial investment of {money_amount} into account, that means you'll make a gross profit of: {gross_profit_compound}\n")
            continue

        # Nested else statement mops up all the other scenarios and prints an error message
        else:
            print("\n!!! Invalid input - Please enter either 'simple' or 'compound'")
            continue

    # Accesses the home loan repayment calculator
    elif calculation_type == "bond":

        try:
            # Takes and converts all the required details from user
            present_house_value = float(input("\nEnter the present value of the house: "))
            annual_rate = float(input("\nEnter the annual interest rate as a percentage without the '%' sign: "))
            planned_months = float(input("\nEnter the number of months you plan to take to repay the bond: "))
            dec_monthly_rate = (annual_rate / 100) / 12

            # Does all the required calculations and prints the output
            repayment = (dec_monthly_rate * present_house_value) / (1 - (1 + dec_monthly_rate) ** (- planned_months))
            rounded_repayment = round(repayment, 2)
            print(f"\nThe amount of money you'll have to repay each month is: {rounded_repayment}\n")
            continue

        except ValueError:
            print("\n!!! Invalid input - Please enter a number")
            continue

    # Mops up all the other scenarios and prints an error message
    else:
        print("\n!!! Invalid input - Please enter either 'investment' or 'bond'")
        continue