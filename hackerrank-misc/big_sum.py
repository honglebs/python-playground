# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    sum = 0
    for i in range (0,len(ar)):
        sum = sum + ar[i]
    return sum

print(aVeryBigSum([1, 2, 3, 4, 5]))
print(aVeryBigSum([1, 1]))






