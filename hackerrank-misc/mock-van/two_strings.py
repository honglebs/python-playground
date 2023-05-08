# Two Strings

# given two strings, determine if they share a common substring 
# substring may be as small as one character 

# parameters is s1: a string & s2: another string
# returns a string bool saying "YES" or "NO" if they have substring in common

def twoStrings(s1, s2):
    # for each character (c) in the first string s1
    for c in s1:
        # condition if that char (c) is in s2, return yes
        if c in s2:
            return "YES"
    # iterated through all chars and did not find a common substring, return no
    return "NO"


# note: solution has time complexity of O(n*m) where n & m are lengths of two string
# need more efficient algo for larger inputs (ie. hasing, suffix arrays)

# ====== ANOTHER WAY ====== #

def twoStrings2(s1, s2):
    # Convert the characters in s1 to a set
    set1 = set(s1)

    # Convert the characters in s2 to a set
    set2 = set(s2)

    # Find the intersection of the two sets
    # use set.intersection method to find common elements 
    common = set1.intersection(set2)

    # If there is at least one common character, return "YES"
    if len(common) > 0:
        return "YES"
    # Otherwise, return "NO"
    else:
        return "NO"


#note: example of set.intersection
# set1 = {'a', 'b', 'c'}
# set2 = {'b', 'c', 'd'}
# common = set1.intersection(set2)
# print(common)  # Output: {'b', 'c'}
