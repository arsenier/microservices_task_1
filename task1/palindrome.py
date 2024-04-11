def is_palindrome(inp):
    return inp == inp[::-1]

print(is_palindrome("cat"))
print(is_palindrome("tenet"))