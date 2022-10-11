stadium_capacity = int(input())
total_fans = int(input())

sector_a_fans = 0
sector_b_fans = 0
sector_v_fans = 0
sector_g_fans = 0

for f in range(total_fans):
    fan_sector = input()
    if fan_sector == 'A':
        sector_a_fans += 1
    elif fan_sector == 'B':
        sector_b_fans += 1
    elif fan_sector == 'V':
        sector_v_fans += 1
    elif fan_sector == 'G':
        sector_g_fans += 1

print(f'{sector_a_fans / total_fans * 100:.2f}%')
print(f'{sector_b_fans / total_fans * 100:.2f}%')
print(f'{sector_v_fans / total_fans * 100:.2f}%')
print(f'{sector_g_fans / total_fans * 100:.2f}%')
print(f'{total_fans / stadium_capacity * 100:.2f}%')