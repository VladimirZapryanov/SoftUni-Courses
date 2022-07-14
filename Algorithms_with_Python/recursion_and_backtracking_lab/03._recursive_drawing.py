def recursive_drawing(current_number):
    if current_number == 0:
        return
    print("*" * current_number)
    recursive_drawing(current_number - 1)
    print('#' * current_number)


number = int(input())

recursive_drawing(number)
