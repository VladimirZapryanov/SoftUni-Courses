def find_the_capitals(word):
    capital_list = []
    for w in range(len(word)):
        if word[w].isupper():
            capital_list.append(w)

    return capital_list


word = input()

print(find_the_capitals(word))