numbers_of_pieces = int(input())
piece_dict = {}

for pieces in range(numbers_of_pieces):
    pieces_info = input().split("|")
    piece_dict[pieces_info[0]] = {"composer": pieces_info[1], "key": pieces_info[2]}

commands = input()

while not commands == "Stop":
    data = commands.split("|")
    command = data[0]
    piece = data[1]

    if command == "Add":
        if piece not in piece_dict:
            piece_dict[piece] = {"composer": data[2], "key": data[3]}
            print(f"{piece} by {data[2]} in {data[3]} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command == "Remove":
        if piece in piece_dict:
            print(f"Successfully removed {piece}!")
            del piece_dict[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        if piece in piece_dict:
            piece_dict[piece]["key"] = data[2]
            print(f"Changed the key of {piece} to {data[2]}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    commands = input()

sorted_piece_dict = dict(sorted(piece_dict.items(), key=lambda kvp: (kvp[0], kvp[1]["composer"])))
for el in sorted_piece_dict:
    print(f"{el} -> Composer: {sorted_piece_dict[el]['composer']}, Key: {sorted_piece_dict[el]['key']}")

