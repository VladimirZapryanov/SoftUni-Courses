secret_message = input().split()

for el in secret_message:
    current_word = []
    asci_letter = ""
    for word in el:
        if word.isdigit():
            asci_letter += word
        else:
            current_word.append(word)
    current_word.insert(0, chr(int(asci_letter)))
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print("".join(current_word), end=" ")