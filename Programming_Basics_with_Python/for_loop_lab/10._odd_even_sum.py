n= int(input())
a=0
b=0
for i in range(0,n):
    number = int(input())
    if i % 2:
        a += number
    else:
        b += number
if a == b:
    print("Yes")
    print(f"Sum = {a}")
else:
    sum = a-b
    print("No")
    print(f"Diff = {abs(sum)}")