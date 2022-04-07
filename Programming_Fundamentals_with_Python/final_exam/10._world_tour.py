text = input()

while True:
    command = input()
    if command == "Travel":
        break
    data = command.split(":")
    action = data[0]
    if action == "Add Stop":
        start = int(data[1])
        stop = data[2]
        if start in range(len(text)):
            text = text[:start] + stop + text[start:]
    elif action == "Remove Stop":
        start = int(data[1])
        end = int(data[2])
        if 0 <= end < len(text):
            to_be_removed = text[start:end+1]
            text = text.replace(to_be_removed, '')
    elif action == 'Switch':
        old = data[1]
        new = data[2]
        text = text.replace(old, new)
    print(text)
print(f"Ready for world tour! Planned stops: {text}")
