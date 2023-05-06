# Repeated String

# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s (aba)
#  2. LONG_INTEGER n (10)
#

# ====== NOTES ====== #

# s = aba 
# n = 10 
# aba.aba.aba.a
# 1 2 3 4 5 6 7 (counting how many 'a' there are)



# def repeatedString(s, n):

#     # init a counter, set to 0 to count how many a's
#     count = 0
#     l = len(s)

#     for i in range(0, l):
#         if s[i] == "a":
#             count += 1
    
#     count *= int(n/l)

#     for i in range(0, n % l):
#         if s[i] == "a":
#             count += 1

#     return count

def repeatedString(s, n):

    # init a count to 0 to count how many a's is there
    count = 0

    # l will be the length of the string (aba --> 3)
    l = len(s)

    # iterate for each i in the length
    for i in range(l):

        # condition for if the iteration is equal to a, count + 1
        if s[i] == "a":
            count += 1

    # // --> keep the whole int, round down (pic)
    count *= n // l

    # this is to handle the remainder of division (ie. aba.aba.aba.a)
    for i in range(n % l):

        # condition for if the iteration of the remainder is equal to a, count + 1
        if s[i] == "a":
            count += 1

    # this was suppose to fix it but it did not, edge case if if len(s) or s? is > n
    return count if l <= n else s[:n].count("a")


print(repeatedString("aba", 10))
print(repeatedString("noneb", 300))
print(repeatedString("aa", 7))
#                     aa.aa.aa.a --> 3.5 --> 3
print(repeatedString("ba", 12))
#                     ba.ba.ba.ba.ba.ba
print(repeatedString("aa", 2))
