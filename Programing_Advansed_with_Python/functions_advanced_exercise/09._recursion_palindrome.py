def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"
    if not word[idx] == word[len(word) - 1 - idx]:
        return f"{word} is not a palindrome"
    return palindrome(word, idx + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))

