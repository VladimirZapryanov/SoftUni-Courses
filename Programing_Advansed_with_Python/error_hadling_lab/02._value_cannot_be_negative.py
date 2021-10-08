class ValueCannotBeNegative(Exception):
    pass


n = 5

for _ in range(n):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative("Number is under zero!")

'''
some test:
1
4
-5
3
10
'''

