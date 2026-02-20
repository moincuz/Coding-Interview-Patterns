
def is_palindrome_valid(s: str) -> bool:    
    left, right = 0, len(s) - 1
    while left < right:   
        # Skip non-alphanumeric characters from the left.     
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right.
        while left < right and not s[right].isalnum():
            right -= 1
        # If the characters at the left and right pointers don't
        # match, the string is not a palindrome.
        if s[left] != s[right]:
            return False 
        left += 1
        right -= 1
    return True

print(is_palindrome_valid("A man, a plan, a canal: Panama"))
print(is_palindrome_valid("race a car"))
print(is_palindrome_valid("poiuytrrtyuiop"))
print(is_palindrome_valid("фывапррпавыф"))
print(is_palindrome_valid("ab2a"))