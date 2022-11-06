def oscars_ceremony(hall_rent, statuettes_price, catering_price, voiceover):
    total_expenses = hall_rent + statuettes_price + catering_price + voiceover

    return total_expenses


hall_rent = int(input())
statuettes_price = hall_rent * 0.7
catering_price = statuettes_price * 0.85
voiceover = catering_price / 2

print(f'{oscars_ceremony(hall_rent, statuettes_price, catering_price, voiceover):.2f}')
