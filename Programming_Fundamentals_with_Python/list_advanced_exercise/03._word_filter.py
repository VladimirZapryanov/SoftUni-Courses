text = input().split()

even_text = [el for el in text if len(el) % 2 == 0]
for el in even_text:
    print(el)


