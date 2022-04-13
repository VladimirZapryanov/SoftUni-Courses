<<<<<<< HEAD
def reverse_text(string):
    for x in range(len(string) - 1, -1, -1):
        yield string[x]


for char in reverse_text("step"):
    print(char, end='')
=======
def reverse_text(string):
    for x in range(len(string) - 1, -1, -1):
        yield string[x]


for char in reverse_text("step"):
    print(char, end='')
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
