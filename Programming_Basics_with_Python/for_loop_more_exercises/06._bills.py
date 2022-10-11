mounts = int(input())

water_bill_per_month = 20
water_bill_for_all_months = water_bill_per_month * mounts
internet_bill_per_month = 15
internet_bill_for_all_months = internet_bill_per_month * mounts
other_bill_for_all_months = 0
electricity_bill_for_all_months = 0

for m in range(1, mounts + 1):
    electricity_bill_per_month = float(input())
    electricity_bill_for_all_months += electricity_bill_per_month
    other_bill_for_all_months += (electricity_bill_per_month + water_bill_per_month + internet_bill_per_month) * 1.2

average_bill = (water_bill_for_all_months + internet_bill_for_all_months + electricity_bill_for_all_months + other_bill_for_all_months) / mounts

print(f"Electricity: {electricity_bill_for_all_months:.2f} lv")
print(f"Water: {water_bill_for_all_months:.2f} lv")
print(f"Internet: {internet_bill_for_all_months:.2f} lv")
print(f"Other: {other_bill_for_all_months:.2f} lv")
print(f"Average: {average_bill:.2f} lv")
