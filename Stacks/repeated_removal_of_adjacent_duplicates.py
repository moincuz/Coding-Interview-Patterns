#20260221


def repeated_removal_of_adjacent_duplicates(s: str) -> str:
    stack = []
    for c in s:
        # If the current character is the same as the top character on the stack,
        # a pair of adjacent duplicates has been formed. So, pop the top character 
        # from the stack.
        if stack and c == stack[-1]:
            stack.pop()
        # Otherwise, push the current character onto the stack.
        else:
            stack.append(c)
    # Return the remaining characters as a string.
    return ''.join(stack)

print(repeated_removal_of_adjacent_duplicates("abbaca"))
print(repeated_removal_of_adjacent_duplicates("azxxzy"))
print(repeated_removal_of_adjacent_duplicates("aababaab"))
print(repeated_removal_of_adjacent_duplicates("aaaa"))
print(repeated_removal_of_adjacent_duplicates("abba"))
print(repeated_removal_of_adjacent_duplicates("abcba"))
print(repeated_removal_of_adjacent_duplicates("abccba"))
print(repeated_removal_of_adjacent_duplicates("abccba"))

## outcome should be:
# "ca"
# "ay"
# "a"
# ""
# ""
# "a"
# "a"
# "a"