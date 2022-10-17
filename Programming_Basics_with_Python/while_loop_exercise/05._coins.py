def bg_coins_count(money):
    bgn, coins = str(money).split('.')
    all_coins = int(bgn) * 100 + int(coins)
    coins_count = 0

    while not all_coins == 0:
        if all_coins >= 200:
            new_coins = all_coins // 200
            coins_count += new_coins
            all_coins -= new_coins * 200
        elif all_coins >= 100:
            new_coins = all_coins // 100
            coins_count += new_coins
            all_coins -= new_coins * 100
        elif all_coins >= 50:
            new_coins = all_coins // 50
            coins_count += new_coins
            all_coins -= new_coins * 50
        elif all_coins >= 20:
            new_coins = all_coins // 20
            coins_count += new_coins
            all_coins -= new_coins * 20
        elif all_coins >= 10:
            new_coins = all_coins // 10
            coins_count += new_coins
            all_coins -= new_coins * 10
        elif all_coins >= 5:
            new_coins = all_coins // 5
            coins_count += new_coins
            all_coins -= new_coins * 5
        elif all_coins >= 2:
            new_coins = all_coins // 2
            coins_count += new_coins
            all_coins -= new_coins * 2
        elif all_coins >= 1:
            new_coins = all_coins // 1
            coins_count += new_coins
            all_coins -= new_coins * 1

    return coins_count


money = float(input())

print(bg_coins_count(money))