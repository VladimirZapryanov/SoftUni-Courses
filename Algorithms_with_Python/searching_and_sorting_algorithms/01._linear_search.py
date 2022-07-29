def search_item(items, searched_item):
    if searched_item in items:
        return 'Yes'
    return 'No'


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
searched_item = int(input())

print(search_item(items, searched_item))