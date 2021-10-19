from collections import deque

bomb_effect = deque([int(el) for el in input().split(", ")])
bomb_casing = [int(el) for el in input().split(", ")]

bombs = {
    "datura": 0,
    "cherry": 0,
    "smoke_decoy": 0
}

bombs_pouch = False

while bomb_effect and bomb_casing:
    be = bomb_effect.popleft()
    bc = bomb_casing.pop()
    if be + bc == 40:
        bombs["datura"] += 1
    elif be + bc == 60:
        bombs["cherry"] += 1
    elif be + bc == 120:
        bombs["smoke_decoy"] += 1
    else:
        bomb_effect.appendleft(be)
        bomb_casing.append(bc - 5)

    if all([el >= 3 for el in bombs.values()]):
        bombs_pouch = True
        break


if bombs_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effect])}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casing])}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {bombs['cherry']}")
print(f"Datura Bombs: {bombs['datura']}")
print(f"Smoke Decoy Bombs: {bombs['smoke_decoy']}")






