# Counting Camelcase 

#function takes in a STRING as parameter 
# function is expected to return an INTEGER

# ====== NOTES ======= #
# oneTwoThree → 3
# thisIsAnExampleOfCamelCase → 7

def camelcase(s):
    # init count, start at 1 since counting first word is lowercase oneTwoThree
    count = 1

    # for each character in string
    for c in s:
        # conditional if the character is uppercase, add 1 to the counter
        if c.isupper():
            count += 1

    # return count of words
    return count

print(camelcase("oneTwoThree"))
print(camelcase("thisIsTheSuperLongString"))

