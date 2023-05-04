# Panagram

# A panagram is a string that contains every letter of the alphabet.
# Given a sentience, determine if its a panagram, return either pangram or not pangram

# "We promptly judged antique ivory buckles for the next prize" --> pangram
# "We promptly judged antique ivory buckles for the prize" --> not pangram (missing x)

# "we promptly judged" --> words_list = [we, promptly, judged]

def pangram(s):
    # create a set that contains all lowercase letter of the alphabet 
    # sets are unordered collections of unique elements 
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    # string (s) is convered to lowercase 
    s = s.lower()

    # the spaces in the string is replaced with the .replace(original, change, occurence)
    # and the string (s) is converted to a set() making it unique (no repeats)
    s = set(s.replace(" ", ""))

    # condition if string (s) is equal to the set of aplhabet 
    # note: only care about all the letters present in the string (s) equal to alphabet, not order
    if s == alphabet:
        return "pangram"
    else:
        return "not pangram"
    

print(pangram("We promptly judged antique ivory buckles for the next prize"))
print(pangram("im not a pangram"))




# ANOTHER WAY # (without typing out the alphabet lol)

def pangrams(s):
    # Create an empty list to hold the letters that are present in the input string
    present_letters = []

    # Iterate through each character in the input string
    for c in s:
        
        # If the character is a letter and is not already in the list of present letters, add it to the list
        if c.isalpha() and c.lower() not in present_letters:
            present_letters.append(c.lower())

    # If the length of the list of present letters is 26 (the number of letters in the alphabet), return "pangram".
    # Otherwise, return "not pangram".
    if len(present_letters) == 26:
        return "pangram"
    else:
        return "not pangram"
