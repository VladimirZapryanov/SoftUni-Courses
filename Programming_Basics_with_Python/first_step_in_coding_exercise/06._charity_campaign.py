number_of_days = int(input())
number_of_chefs = int(input())
number_of_cakes = int(input()) * 45
number_of_waffles = int(input()) * 5.80
number_of_pancakes = int(input()) * 3.20
donation_from_one_chef = number_of_cakes + number_of_waffles + number_of_pancakes
donation_per_day = donation_from_one_chef * number_of_chefs
all_donation = donation_per_day * number_of_days
final_donation = all_donation - (all_donation / 8)
print(final_donation)