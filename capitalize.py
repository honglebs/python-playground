
# "hong le" --> "Hong Le"
# .split "hong le" --> "hong" "le"
# .capitalize() --> "Hong"
# .replace(orginal string, the chnage, how many times)


# s = "hong le"

def capitalize(s):
    # use split() the input string s into a list of words --> words_list = ["hong", "le"]
    words_list = s.split()

    # loop through each word in the list
    for word in words_list: 
        # capitialize the first letter of the word with capitalize()
        capitalized_word = word.capitalize()

        #replace() the original word in the input string with capitialzed version
        s = s.replace(word, capitalized_word)
    
    # return the modified input string with first letter capitialized 
    return s

print(capitalize("hong le"))
print(capitalize("will this work please capitalize"))