n= int(input())
a=0
b=0
for i in range(0,n):
    number = int(input())
    a += number
for i in range (0,n):
    number = int(input())
    b += number
if a == b:
    print(f"Yes, sum = {a}")
else:
    sum = a-b
    print(f"No, diff = {abs(sum)}")