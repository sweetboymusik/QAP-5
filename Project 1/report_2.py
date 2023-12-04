# Report 2 - Monthly Payment Listing (Exception Report)
# For One Stop Insurance Company
# Date Written: November 30, 2023 - December 04, 2023
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
HST_RATE = float(defaults.readline().strip())
PROCESS_RATE = float(defaults.readline().strip())
defaults.close()

TODAY = datetime.date.today().strftime("%d-%b-%y")


# define functions
def format_dollars_1(amt):
    fmt1 = f"${amt:,.2f}"
    fmt2 = f"{fmt1:>9s}"

    return fmt2


def format_dollars_2(amt):
    fmt1 = f"${amt:,.2f}"
    fmt2 = f"{fmt1:>10s}"

    return fmt2


def format_dollars_3(amt):
    fmt1 = f"${amt:,.2f}"
    fmt2 = f"{fmt1:>7s}"

    return fmt2


# report header
# there are some slight adjustments from the QAP5 document
# as HST totals overflowed from the 7 characters outlined
print()
print("ONE STOP INSURANCE COMPANY")
print(f"MONTHLY PAYMENT LISTING AS OF {TODAY}")
print()
print(
    f"POLICY {'CUSTOMER':<20s} {'TOTAL':<12s}{' ' * 7}{'TOTAL':<10s}{'DOWN':<8s} MONTHLY")
print(
    f"NUMBER {'NAME':<20s}{'PREMIUM':<12s}{'HST':<8}{'COST':<9s}{'PAYMENT':<9} PAYMENT")
print("=" * 73)


# import values from file
policies = open("Policies.dat", "r")

# counters and accumulators
policy_cnt = 0
premium_acum = 0
taxes_acum = 0
total_acum = 0
dp_acum = 0
mp_acum = 0

for line in policies:
    entries = line.split(", ")

    policy_num = entries[0].strip()
    cust_fname = entries[2].strip()
    cust_lname = entries[3].strip()
    num_cars = int(entries[9].strip())
    liability_opt = entries[10].strip().upper()
    glass_opt = entries[11].strip().upper()
    loan_opt = entries[12].strip().upper()
    payment_type = entries[13].strip().lower()
    down_payment = float(entries[14].strip().lower())

    # exception check
    if (payment_type != "down pay") and (payment_type != "monthly"):
        continue

    # calculations
    insurance_premium = PREMIUM_RATE
    if num_cars > 1:
        insurance_premium += (PREMIUM_RATE * DISCOUNT_RATE) * (num_cars - 1)

    extra_costs = 0
    if liability_opt == "Y":
        extra_costs += LIABILITY_RATE * num_cars
    if glass_opt == "Y":
        extra_costs += GLASS_RATE * num_cars
    if loan_opt == "Y":
        extra_costs += LOAN_RATE * num_cars

    total_premium = insurance_premium + extra_costs
    taxes = total_premium * HST_RATE
    total = total_premium + taxes

    monthly_payment = (total + PROCESS_RATE - down_payment) / 12

    # output
    print(
        f"{policy_num:4s}  {cust_fname + ' ' +  cust_lname:<19s}{format_dollars_1(total_premium)}   {format_dollars_3(taxes)} {format_dollars_1(total)} {format_dollars_1(down_payment)}{format_dollars_1(monthly_payment)}")

    # increment counters and accumulators
    policy_cnt += 1
    premium_acum += insurance_premium
    taxes_acum += taxes
    total_acum += total_premium
    dp_acum += down_payment
    mp_acum += monthly_payment

policies.close()

# report footer
# as stated in header, HST totals overflow the 7 character limit
print("=" * 73)
print(
    f"Total policies: {policy_cnt:03d} {' ' * 5}{format_dollars_1(premium_acum)} {format_dollars_1(taxes_acum)} {format_dollars_1(total_acum)} {format_dollars_1(dp_acum)}{format_dollars_1(mp_acum)}")
