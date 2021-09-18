text = input()

symbols = {}

for el in text:
    if el not in symbols:
        symbols[el] = 1
    else:
        symbols[el] += 1

sort_symbols = sorted(symbols)

[print(f"{el}: {symbols[el]} time/s") for el in sort_symbols]