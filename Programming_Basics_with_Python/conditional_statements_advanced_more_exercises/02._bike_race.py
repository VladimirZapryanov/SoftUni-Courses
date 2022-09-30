def bike_race_donate(fee, cross_country_people_discount, discount, juniors_bikers, seniors_bikers, type_of_track, junior_trail_price, junior_cross_country_price, junior_downhill_price, junior_road_price, senior_trail_price, senior_cross_country_price, senior_downhill_price, senior_road_price):
    donate_money = 0

    if type_of_track == 'trail':
        donate_money = juniors_bikers * junior_trail_price + seniors_bikers * senior_trail_price
    elif type_of_track == 'cross-country':
        if juniors_bikers + seniors_bikers >= cross_country_people_discount:
            junior_cross_country_price = junior_cross_country_price - (junior_cross_country_price * discount)
            senior_cross_country_price = senior_cross_country_price - (senior_cross_country_price * discount)
            donate_money = juniors_bikers * junior_cross_country_price + seniors_bikers * senior_cross_country_price
        else:
            donate_money = juniors_bikers * junior_cross_country_price + seniors_bikers * senior_cross_country_price
    elif type_of_track == 'downhill':
        donate_money = juniors_bikers * junior_downhill_price + seniors_bikers * senior_downhill_price
    elif type_of_track == 'road':
        donate_money = juniors_bikers * junior_road_price + seniors_bikers * senior_road_price

    donate_money = donate_money - (donate_money * fee)

    return f'{donate_money:.2f}'


juniors_bikers = int(input())
seniors_bikers = int(input())
type_of_track = input()

cross_country_people_discount = 50
discount = 25 / 100
fee = 5 / 100

junior_trail_price = 5.50
junior_cross_country_price = 8
junior_downhill_price = 12.25
junior_road_price = 20

senior_trail_price = 7
senior_cross_country_price = 9.50
senior_downhill_price = 13.75
senior_road_price = 21.50


print(bike_race_donate(fee, cross_country_people_discount, discount, juniors_bikers, seniors_bikers, type_of_track, junior_trail_price, junior_cross_country_price, junior_downhill_price, junior_road_price, senior_trail_price, senior_cross_country_price, senior_downhill_price, senior_road_price))
