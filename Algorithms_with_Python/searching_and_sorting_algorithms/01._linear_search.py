def search_item(numbers, target):
    if target in numbers:
        return 'Yes'
    return 'No'


numbers = [int(x) for x in input().split(' ')]
target = int(input())

print(search_item(numbers, target))