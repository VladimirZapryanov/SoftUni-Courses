symbol = input()
secret_letters = []
secret_message = ''

while not symbol == 'End':
    if not symbol.isalpha():
        symbol = input()
        continue
    if symbol == 'c' or symbol == 'o' or symbol == 'n':
        if symbol not in secret_letters:
            secret_letters.append(symbol)
            if 'c' in secret_letters and 'o' in secret_letters and 'n' in secret_letters:
                print(secret_message, end=' ')
                secret_message = ''
                secret_letters = []
        else:
            secret_message += symbol
    else:
        secret_message += symbol

    symbol = input()