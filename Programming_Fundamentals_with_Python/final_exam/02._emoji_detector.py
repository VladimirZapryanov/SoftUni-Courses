import re

pattern_emoji = r"(?P<separator>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=separator)"
pattern_num = r"\d"

text = input()
cool_threshold = 1

numbers = re.findall(pattern_num, text)

for num in numbers:
    num = int(num)
    cool_threshold *= num

print(f"Cool threshold: {cool_threshold}")

emoji = re.finditer(pattern_emoji, text)
emoji_count = 0
cool_emoji = []

for em in emoji:
    emoji_count += 1
    current_emoji = em.groupdict()
    emoji = current_emoji["emoji"]
    emoji_coolness = sum([ord(letter) for letter in emoji])
    if emoji_coolness >= cool_threshold:
        cool_emoji.append(f"{current_emoji['separator']}{current_emoji['emoji']}{current_emoji['separator']}")

print(f"{emoji_count} emojis found in the text. The cool ones are:")
for i in cool_emoji:
    print(i)
