n = int(input())

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(f"{chr(i + 97)}{chr(j + 97)}{chr(k + 97)}")