age = int(input())

if age <= 14:
    print("drink toddy")
elif age > 14 and age <= 18:
    print("drink coke")
elif age > 18 and age <= 21:
    print("drink beer")
else:
    print("drink whisky")

#another way !!!
#ages = int(input())
#drink = ""
#if ages <= 14:
#    drink = "toddy"
#elif ages <= 18:
#    drink = "coke"
#elif ages<= 21:
#    drink = "beer"
#else:
#    drink = "whisky"
#print(f"drink {drink}")