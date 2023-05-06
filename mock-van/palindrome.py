# Palindrome Index

# a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# given a string of lowercase letters range ascii[a-z]
# determine the index of a chracter that can be removed to make the string a palindrome

# parameter is a string, return int (the index of which the chracter that needs to be removed)

# ======= NOTES ======= #
# aaab --> [3] 
# baa --> [0]
# aaa --> [-1]

def palindromeIndex(s):
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return -1

    # Find the length of the string
    n = len(s)

    # Iterate through the string
    for i in range(n):
        # Try removing each character and check if the resulting string is a palindrome
        t = s[:i] + s[i+1:]
        if t == t[::-1]:
            # If the resulting string is a palindrome, return the index of the removed character
            return i

    # If no single character can be removed to make the string a palindrome, return -1
    return -1


# we try removing it from the string by creating a new string t that is equal to the original string with the current character removed. 
# We then check if the new string t is a palindrome by comparing it to its reversed version. 
# If t is a palindrome, we immediately return the index of the removed character



# ANOTHER WAY BUT ITS USING POINTERS, IS OPTIMIZED #
def palindromeIndex(s):
    n = len(s)
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return -1

    # Initialize pointers
    left, right = 0, n - 1

    while left < right:
        # Check if characters at the left and right pointers match
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # If the characters do not match, try removing one of them
            # and check if the resulting string is a palindrome
            t1 = s[:left] + s[left+1:]
            t2 = s[:right] + s[right+1:]

            if t1 == t1[::-1]:
                return left
            elif t2 == t2[::-1]:
                return right
            else:
                # If neither resulting string is a palindrome, the string
                # cannot be made into a palindrome by removing a single character
                return -1

    # If we reached this point, the string is already a palindrome
    return -1
