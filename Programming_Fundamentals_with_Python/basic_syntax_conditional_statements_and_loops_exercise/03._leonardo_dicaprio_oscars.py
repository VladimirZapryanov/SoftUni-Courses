n = int(input())
oscar_result = ""

if n == 88:
    oscar_result = "Leo finally won the Oscar! Leo is happy"
elif n == 86:
    oscar_result = "Not even for Wolf of Wall Street?!"
elif n < 88:
    oscar_result = "When will you give Leo an Oscar?"
elif n > 88:
    oscar_result = "Leo got one already!"

print(oscar_result)
