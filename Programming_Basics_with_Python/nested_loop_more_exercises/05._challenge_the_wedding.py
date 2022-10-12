men = int(input())
women = int(input())
table = int(input())

for m in range(1, men + 1):
    for w in range(1, women + 1):
        if table <= 0:
            break
        table -= 1
        print(f'({m} <-> {w})', end=' ')