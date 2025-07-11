def isPalindrome(x):
    # Negative numbers or numbers ending in 0 (but not 0 itself) can't be palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    rev = 0
    while x > rev:
        last_digit = x % 10
        rev = rev * 10 + last_digit
        x = x // 10

    # x == rev for even-length, x == rev//10 for odd-length
    return x == rev or x == rev // 10

# Test cases
print(isPalindrome(121))    # True
print(isPalindrome(-121))   # False
print(isPalindrome(10))     # False
print(isPalindrome(1221))   # True
print(isPalindrome(0))      # True
print(isPalindrome(12321))  # True