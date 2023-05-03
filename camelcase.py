#counting camelcase 
#function takes in a STRING as parameter 
# function is expected to return an INTEGER

def camelcase(s):
    count = 1
    for c in s:
        if c.isupper():
            count += 1
    return count
print(camelcase("oneTwoThree"))