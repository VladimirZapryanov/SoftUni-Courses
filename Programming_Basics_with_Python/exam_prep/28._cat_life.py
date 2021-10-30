cat_kind = str(input())
gender_cat = str(input())
live_cat = 0
live_cat_person = 0

if cat_kind not in ("British Shorthair", "Siamese", "Persian", "Ragdoll", "American Shorthair", "Siberian"):
    print(f"{cat_kind} is invalid cat!")
elif cat_kind == "British Shorthair" and gender_cat == "m":
    live_cat_person = 13
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "British Shorthair" and gender_cat == "f":
    live_cat_person = 14
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "Siamese" and gender_cat == "m":
    live_cat_person = 15
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "Siamese" and gender_cat == "f":
    live_cat_person = 16
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "Persian" and gender_cat == "m":
    live_cat_person = 14
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "Persian" and gender_cat == "f":
    live_cat_person = 15
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "Ragdoll" and gender_cat == "m":
    live_cat_person = 16
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "Ragdoll" and gender_cat == "f":
    live_cat_person = 17
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "American Shorthair" and gender_cat == "m":
    live_cat_person = 12
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "American Shorthair" and gender_cat == "f":
    live_cat_person = 13
    live_cat = round(live_cat_person * 12 / 6)
elif cat_kind == "Siberian" and gender_cat == "m":
    live_cat_person = 11 * 12
    live_cat = round(live_cat_person / 6)
elif cat_kind == "Siberian" and gender_cat == "f":
    live_cat_person = 12 * 12
    live_cat = round(live_cat_person / 6)

if live_cat > 0:
    print(f"{live_cat} cat months")






