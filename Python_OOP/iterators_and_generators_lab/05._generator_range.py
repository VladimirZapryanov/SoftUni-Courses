<<<<<<< HEAD
def genrange(start, end):
    for x in range(start, end + 1):
        yield x


=======
def genrange(start, end):
    for x in range(start, end + 1):
        yield x


>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
print(list(genrange(1, 10)))