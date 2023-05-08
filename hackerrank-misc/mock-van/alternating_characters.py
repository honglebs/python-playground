# Alternating Characters 

# given a string containing characters A and B only
# task is to chnage it into a string that does NOT have matching adjacent characters
# to do this, you are allowed to delete 0 or many chars in the string

# task is to find the minimum number of required deletions

# ====== NOTES ====== #

# parameters is going to be string (s), returns int (the min number of deletions required)
# ABBAB --> delete second B to get ABAB

# iterate through the string and compare each character to its adjacent char 


def alternatingCharacters(s):

    # init a count to 0 and prev to an empty string
    count = 0
    prev = ''

    # iterate for each char in s if char is eqal to prev (A == A), then count + 1
    for char in s:
        if char == prev:
            count += 1
        
        # if they are different, we update our prev char to current char and continue iterating
        else:
            prev = char
    return count 