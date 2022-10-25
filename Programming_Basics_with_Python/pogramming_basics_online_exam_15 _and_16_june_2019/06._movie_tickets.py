a1 = int(input())
a2 = int(input())
n = int(input())

s3_range = int(n / 2 - 1)
for s1 in range(a1, a2):
    if s1 % 2 == 1:
        symbol = chr(s1)
        for s2 in range(1, n):
            for s3 in range(1, s3_range + 1):
                s4 = ord(symbol)
                score = s2 + s3 + s4
                if score % 2 == 1:
                    print(f'{symbol}-{s2}{s3}{s4}')
