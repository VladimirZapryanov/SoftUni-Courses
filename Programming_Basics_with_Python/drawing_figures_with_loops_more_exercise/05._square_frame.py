number = int(input())

print('+ ' + '- ' * (number - 2) + '+')
for s in range(number - 2):
    print('| ' + '- ' * (number - 2) + '|')
print('+ ' + '- ' * (number - 2) + '+')
