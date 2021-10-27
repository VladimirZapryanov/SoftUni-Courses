bitcoin_count = int(input())
chinese_count = float(input())
commission = float(input())

bitcoin_price = bitcoin_count * 1168
chinese_price_usd = chinese_count * 0.15
chinese_price_lv = chinese_price_usd * 1.76
price_euro = (bitcoin_price + chinese_price_lv) / 1.95
total_price = price_euro - price_euro * (commission / 100)

print(f"{total_price:.2f}")
