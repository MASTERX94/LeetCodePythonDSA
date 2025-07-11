# def isPalindrome(x):
#     s= str(x)
#     rev= s[::-1]
#     if (s==rev):
#         return True
#     else:
#         return False
    
# print(isPalindrome(1231))

#  All -ve number are not palindrome 
#  This Approach req extra non constant space for creating string

# print(1221%10)        #Output = 1
# print(1221//10)       #Output = 122
# a=125 
# a=a/10
# print(a)               #Output = 12.5

"""
Check if an integer is a palindrome without converting it to a string.

A palindrome number reads the same backward as forward, e.g., 121 or 1221.
This solution avoids extra non-constant space usage by reversing only half of the number.
"""

def isPalindrome(x):
    # Negative numbers and numbers ending with 0 (but not 0 itself) can't be palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0

    # Reverse only the second half of the number
    while x > reversed_half:
        last_digit = x % 10
        reversed_half = reversed_half * 10 + last_digit
        x = x // 10

    # For even-length numbers: x == reversed_half
    # For odd-length numbers: x == reversed_half // 10 (to remove the middle digit)
    return x == reversed_half or x == reversed_half // 10