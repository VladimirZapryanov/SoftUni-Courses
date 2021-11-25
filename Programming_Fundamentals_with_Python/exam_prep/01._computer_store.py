prices = input()
price_without_taxes = 0

while not (prices == "special" or prices == "regular"):
    prices = float(prices)
    if prices < 0:
        print("Invalid price!")
    else:
        price_without_taxes += prices
    prices = input()

taxes = price_without_taxes * 0.2
total_price = price_without_taxes + taxes

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if prices == "special":
        special_total_price = total_price - total_price * 0.1
        print(f"Total price: {special_total_price:.2f}$")
    else:
        print(f"Total price: {total_price:.2f}$")