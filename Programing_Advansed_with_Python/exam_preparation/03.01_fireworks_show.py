from collections import deque

fireworks_effects = deque([int(el) for el in input().split(", ") if int(el) > 0])
explosive_power = [int(el) for el in input().split(", ") if int(el) > 0]

fireworks = {
    "palm": 0,
    "willow": 0,
    "crossette": 0
}

perfect_fireworks_show = False

while fireworks_effects and explosive_power:
    fe = fireworks_effects.popleft()
    ep = explosive_power.pop()
    score = fe + ep
    if score % 3 == 0 and score % 5 == 0:
        fireworks["crossette"] += 1
    elif score % 3 == 0:
        fireworks["palm"] += 1
    elif score % 5 == 0:
        fireworks["willow"] += 1
    else:
        decrease_value = fe - 1
        if decrease_value > 0:
            fireworks_effects.append(decrease_value)
        explosive_power.append(ep)

    if fireworks["palm"] >= 3 and fireworks["willow"] >= 3 and fireworks["crossette"] >= 3:
        perfect_fireworks_show = True
        break

if perfect_fireworks_show:
    print("Congrats! You made the perfect firework show!")
    if fireworks_effects:
        print(f"Firework Effects left: {', '.join(str(el) for el in fireworks_effects)}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")
    print(f"Palm Fireworks: {fireworks['palm']}")
    print(f"Willow Fireworks: {fireworks['willow']}")
    print(f"Crossette Fireworks: {fireworks['crossette']}")

else:
    print("Sorry. You can't make the perfect firework show.")
    if fireworks_effects:
        print(f"Firework Effects left: {', '.join(str(el) for el in fireworks_effects)}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")
    print(f"Palm Fireworks: {fireworks['palm']}")
    print(f"Willow Fireworks: {fireworks['willow']}")
    print(f"Crossette Fireworks: {fireworks['crossette']}")

