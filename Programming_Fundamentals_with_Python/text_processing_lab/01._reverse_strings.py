words = input()

while not words == "end":
    new_words = words[::-1]
    print(f"{words} = {new_words}")
    words = input()
