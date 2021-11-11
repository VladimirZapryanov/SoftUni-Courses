import re

pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>[0-9]+[0-9\.]*)!(?P<quantity>[0-9]+)"

command = input()
total_money_spend = 0
furniture_list = []
while not command == "Purchase":
    valid_command = re.finditer(pattern, command)
    for el in valid_command:
        total_money_spend += float(el["price"]) * int(el["quantity"])
        furniture_list.append(el["furniture"])
    command = input()
print("Bought furniture:")
for el in furniture_list:
    print(el)
print(f"Total money spend: {total_money_spend:.2f}")

