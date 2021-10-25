words = input().split()
searched_palindrome = input()
palindrome = [el for el in words if el[::-1] == el]
print(palindrome)
print(f"Found palindrome {palindrome.count(searched_palindrome)} times")
