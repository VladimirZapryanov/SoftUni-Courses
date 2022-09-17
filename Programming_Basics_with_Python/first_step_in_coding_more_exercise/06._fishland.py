def needed_money(bonito_kilograms , bonito_price_per_kilogram, saffron_kilograms, saffron_price_per_kilogram, mussels_kilograms, mussels_price_per_kilogram):
    return f'{(bonito_kilograms * bonito_price_per_kilogram) + (saffron_kilograms * saffron_price_per_kilogram) + (mussels_kilograms * mussels_price_per_kilogram):.2f}'


mackereL_price_per_kilogram = float(input())
sprat_price_per_kilogram = float(input())
bonito_kilograms = float(input())
saffron_kilograms = float(input())
mussels_kilograms = float(input())

bonito_price_per_kilogram = mackereL_price_per_kilogram * 1.6
saffron_price_per_kilogram = sprat_price_per_kilogram * 1.8
mussels_price_per_kilogram = 7.50

print(needed_money(bonito_kilograms, bonito_price_per_kilogram, saffron_kilograms, saffron_price_per_kilogram, mussels_kilograms, mussels_price_per_kilogram))