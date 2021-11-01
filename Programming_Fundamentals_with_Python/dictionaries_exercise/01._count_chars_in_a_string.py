words = input()

words_dict = {}

for w in words:
    if w not in words_dict:
        words_dict[w] = 1
    else:
        words_dict[w] += 1

if " " in words_dict:
    del words_dict[" "]

for letter, count in words_dict.items():
    print(f"{letter} -> {count}")


