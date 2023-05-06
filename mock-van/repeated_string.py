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
    count = 0
    l = len(s)

    for i in range(l):
        if s[i] == "a":
            count += 1

    count *= n // l

    for i in range(n % l):
        if s[i] == "a":
            count += 1

    return count


print(repeatedString("aba", 10))
print(repeatedString("noneb", 300))
print(repeatedString("aa", 1))