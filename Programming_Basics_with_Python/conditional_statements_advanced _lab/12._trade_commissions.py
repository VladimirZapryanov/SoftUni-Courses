name_of_city = input()
sales = float(input())
commissions = 0
if not name_of_city in ("Sofia, Varna, Plovdiv"):
    print("error")
    exit()
if sales < 0:
    print("error")
    exit()
if name_of_city == "Sofia":
    if 0 <= sales <= 500:
        commissions = sales * 0.05
    elif 500 < sales <= 1000:
        commissions = sales * 0.07
    elif 1000 < sales <= 10000:
        commissions = sales * 0.08
    elif sales > 10000:
        commissions = sales * 0.12
    print(f"{commissions:.2f}")
elif name_of_city == "Varna":
    if 0 <= sales <= 500:
        commissions = sales * 0.045
    elif 500 < sales <= 1000:
        commissions = sales * 0.075
    elif 1000 < sales <= 10000:
        commissions = sales * 0.10
    elif sales > 10000:
        commissions = sales * 0.13
    print(f"{commissions:.2f}")
elif name_of_city == "Plovdiv":
    if 0 <= sales <= 500:
        commissions = sales * 0.055
    elif 500 < sales <= 1000:
        commissions = sales * 0.08
    elif 1000 < sales <= 10000:
        commissions = sales * 0.12
    elif sales > 10000:
        commissions = sales * 0.145
    print(f"{commissions:.2f}")


