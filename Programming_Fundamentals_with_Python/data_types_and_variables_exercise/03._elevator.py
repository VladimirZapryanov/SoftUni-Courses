import math

people = int(input())
capacity = int(input())

courses = math.ceil(people / capacity)

print(courses)
