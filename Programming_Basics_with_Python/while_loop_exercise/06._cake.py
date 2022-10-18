cake_width = int(input())
cake_length = int(input())
command = input()

cake_size = cake_length * cake_width
while not command == 'STOP':
    cake_pieces = int(command)
    cake_size -= cake_pieces
    if cake_size < 0:
        print(f'No more cake left! You need {abs(cake_size)} pieces more.')
        break

    command = input()

if cake_size >= 0:
    print(f'{cake_size} pieces are left.')