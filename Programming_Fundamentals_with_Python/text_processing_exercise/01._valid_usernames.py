usernames = input().split(", ")

for name in usernames:
    if 3 <= len(name) <= 16:
        if name.isalnum() or "-" in name or "_" in name:
            print(name)
