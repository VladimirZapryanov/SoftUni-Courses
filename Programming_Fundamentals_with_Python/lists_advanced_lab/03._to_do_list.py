to_do_list = [0] * 10
notes = input()

while not notes == "End":
    importance, text = notes.split("-")
    current_index = int(importance) - 1
    to_do_list[current_index] = text
    notes = input()

print([el for el in to_do_list if not el == 0])


