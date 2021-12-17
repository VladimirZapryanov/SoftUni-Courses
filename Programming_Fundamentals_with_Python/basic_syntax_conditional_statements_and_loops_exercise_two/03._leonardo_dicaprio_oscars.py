number = int(input())
messages = ""

if number == 88:
    messages = "Leo finally won the Oscar! Leo is happy"
elif number == 86:
    messages = "Not even for Wolf of Wall Street?!"
elif 88 > number:
    messages = "When will you give Leo an Oscar?"
elif number > 88:
    messages = "Leo got one already!"

print(messages)
