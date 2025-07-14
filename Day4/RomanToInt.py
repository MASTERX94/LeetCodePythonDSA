def romanToint(s: str):
    # Dictionary to map Roman numerals to their integer values
    translations = {
        "I": 1, "V": 5, "X": 10, "L": 50, 
        "C": 100, "D": 500, "M": 1000
    }

    number = 0  # Initialize the total number

    # Replace subtractive notation with additive equivalent
    s = s.replace("IV", "IIII")   # 4 = 1 + 1 + 1 + 1
    s = s.replace("IX", "VIIII")  # 9 = 5 + 1 + 1 + 1 + 1
    s = s.replace("XL", "XXXX")   # 40 = 10 + 10 + 10 + 10
    s = s.replace("XC", "LXXXX")  # 90 = 50 + 10 + 10 + 10 + 10
    s = s.replace("CD", "CCCC")   # 400 = 100 * 4
    s = s.replace("CM", "DCCCC")  # 900 = 500 + 100 * 4

    # Convert the transformed Roman numeral to an integer
    for char in s:
        number += translations[char]

    return number

print(romanToint("MCMXCIV"))  # Output: 1994
