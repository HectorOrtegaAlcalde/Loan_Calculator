#-------------------------------------------------------------------------------
# Name:        Loan calculator
# Purpose:     Project from JetBrains academy
#
# Author:      Hector
#
# Created:     22/07/2022
# Copyright:   (c) Hecto 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import sys
import argparse

####################################################

def nominal_interest_rate(loan_interest):
    return loan_interest / 1200

def number_of_months(P, monthly_payment, i):
    body = monthly_payment / (monthly_payment - (i * P))
    return math.ceil(math.log(body, 1 + i))

def annuity_payment(i, P, n):
    numerator = P * i * pow(1 + i, n)
    denominator = pow(1 + i, n) - 1
    return numerator / denominator

def loan_principal(A, i, n):
    denominator = (i * pow(1 + i, n)) / (pow(1 + i, n) - 1)
    return A / denominator

def diff_payment(P, i, periods, m):
    return (P / periods) + i * (P - (P * (m - 1)) / periods)

##################################################


parser = argparse.ArgumentParser(description="This program is a credit calculator.")
parser.add_argument("--type", required = True, choices=['diff', 'annuity'])
parser.add_argument('--principal', type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
args = parser.parse_args()
if len(sys.argv) < 5:
    print("Incorrect parameters.")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters.")
elif args.payment is not None and args.payment < 0:
    print("Incorrect parameters.")
elif args.principal is not None and args.principal < 0:
    print("Incorrect parameters.")
elif args.periods is not None and args.periods < 0:
    print("Incorrect parameters.")
elif args.interest is None or args.interest < 0:
    print("Incorrect parameters.")
elif args.type == "diff":
    if args.principal is not None and args.periods is not None:
        i = nominal_interest_rate(args.interest)
        sum_ = 0
        for j in range(1, args.periods + 1):
            D_m = diff_payment(args.principal, i, args.periods, j)
            D_m = math.ceil(D_m)
            sum_ += D_m
            print(f"Month {j}: payment is {D_m}")
        overpayment = sum_ - args.principal
        print(f"Overpayment = {overpayment}")
elif args.type == "annuity":
    if args.principal is not None and args.payment is not None:
        i = nominal_interest_rate(args.interest)
        overpayment = number_of_months(args.principal, args.payment, i) * args.payment - args.principal
        num_years = number_of_months(args.principal, args.payment, i) // 12
        months_resting = math.ceil(number_of_months(args.principal, args.payment, i) % 12)
        if months_resting == 0:
            print(f"It will take {num_years} years to repay this loan")
        else:
            print(f"It will take {num_years} years and {months_resting} months to repay this loan!")
        print(f"Overpayment = {overpayment}")
    if args.payment is not None and args.periods is not None:
        i = nominal_interest_rate(args.interest)
        loan_principal = loan_principal(args.payment, i, args.periods)
        print(f"Your loan principal = {loan_principal}!")
    if args.principal is not None and args.periods is not None:
        i = nominal_interest_rate(args.interest)
        monthly_payment = math.ceil(annuity_payment(i,args.principal, args.periods))
        print(f"Your monthly payment = {monthly_payment}!")

