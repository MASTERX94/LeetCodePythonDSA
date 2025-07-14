def longestCommonPrefix(strs: list[str]) -> str:
    # Return empty string if the input list is empty
    if not strs:
        return ""

    # Start with the first string as the initial prefix
    prefix = strs[0]

    # Loop through the remaining strings
    for string in strs[1:]:
        # Reduce the prefix until it matches the start of the current string
        while not string.startswith(prefix):
            prefix = prefix[:-1]  # Remove the last character from prefix
            if prefix == "":
                return ""  # No common prefix found

    return prefix  # Final common prefix after checking all strings

print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
