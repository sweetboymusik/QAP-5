# Report 1 - Policy Listing (Detailed Report)
# For One Stop Insurance Company
# Date Written: November 30, 2023
# Author: Elliott Butt

# import libraries
import datetime

# read/define constants
defaults = open("OSICDef.dat", "r")
NEXT_POL_NUM = defaults.readline().strip()
PREMIUM_RATE = float(defaults.readline().strip())
DISCOUNT_RATE = float(defaults.readline().strip())
LIABILITY_RATE = float(defaults.readline().strip())
GLASS_RATE = float(defaults.readline().strip())
LOAN_RATE = float(defaults.readline().strip())
defaults.close()

TODAY = datetime.date.today().strftime("%d-%m-%y")
DATE_FORMAT = "%Y-%m-%d"


# define functions
def format_dollars_1(amt):
    fmt1 = f"${amt:,.2f}"
    fmt2 = f"{fmt1:>9s}"

    return fmt2


def format_dollars_2(amt):
    fmt1 = f"${amt:,.2f}"
    fmt2 = f"{fmt1:>10s}"

    return fmt2


# report header
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF {TODAY}")
print()
print(
    f"POLICY {'CUSTOMER':<24s}{'POLICY':<11s}{'INSURANCE':<14s}{'EXTRA':<10s} TOTAL")
print(
    f"NUMBER {'NAME':<25s}{'DATE':<11s}{'PREMIUM':<13}{'COSTS':<9s} PREMIUM")
print("=" * 73)

# import values from file
policies = open("Policies.dat", "r")

# counters and accumulators
policy_cnt = 0
premium_acum = 0
extra_acum = 0
total_acum = 0

for line in policies:
    entries = line.split(", ")

    policy_num = entries[0].strip()
    policy_date = datetime.datetime.strptime(entries[1].strip(), DATE_FORMAT)
    cust_fname = entries[2].strip()
    cust_lname = entries[3].strip()
    num_cars = int(entries[9].strip())
    liability_opt = entries[10].strip().upper()
    glass_opt = entries[11].strip().upper()
    loan_opt = entries[12].strip().upper()

    # calculations
    insurance_premium = PREMIUM_RATE
    if num_cars > 1:
        insurance_premium += (PREMIUM_RATE * DISCOUNT_RATE) * (num_cars - 1)

    extra_costs = 0
    if liability_opt == "Y":
        extra_costs += LIABILITY_RATE
    if glass_opt == "Y":
        extra_costs += GLASS_RATE
    if loan_opt == "Y":
        extra_costs += LOAN_RATE

    total_premium = insurance_premium + extra_costs

    # output
    print(
        f" {policy_num:4s}  {cust_fname + ' ' +  cust_lname:<20s}  {policy_date.date()}   {format_dollars_1(insurance_premium)}  {format_dollars_1(extra_costs)}  {format_dollars_1(total_premium)}")

    # increment counters and accumulators
    policy_cnt += 1
    premium_acum += insurance_premium
    extra_acum += extra_costs
    total_acum += total_premium

policies.close()

# report footer
print("=" * 73)
print(
    f"Total policies: {policy_cnt:03d} {' ' * 20} {format_dollars_2(premium_acum)} {format_dollars_2(extra_acum)} {format_dollars_2(total_acum)}")
