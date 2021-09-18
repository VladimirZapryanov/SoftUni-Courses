n, m = [int(n) for n in input().split()]

first_set = set()
second_set = set()

for _ in range(n):
    nums = int(input())
    first_set.add(nums)

for _ in range(m):
    nums = int(input())
    second_set.add(nums)

unique_set = first_set.intersection(second_set)
#unique_set = first_set & second_set

[print(n) for n in unique_set]