deposit = float(input())
time_of_deposit = int(input())
yearly_interest_percent = float(input())
interest = deposit * (yearly_interest_percent/100)
monthly_interest = interest / 12
final_money = deposit + (monthly_interest * time_of_deposit)
print(final_money)