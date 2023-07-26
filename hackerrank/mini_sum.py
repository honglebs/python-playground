# Mini Max
# Minimum numbers to solve this

# Given five positive ints, 
# find the minimum and maximum values that can be calaculated by summing exactly
# four of the five integers

# arr = [1, 3, 5, 7, 9]
# the minimum sum is 1 + 3 + 5 + 7 = 16
# the maximum sun is 3 + 5 + 7 + 9 = 24
# the function would print 16 24

def miniMaxSum(arr):
    #1 sort the array in ascending order
    arr.sort()

    #2 calculate the sum of all elements
    total_sum = sum(arr)

    #3 find the minimum sum
    min_sum = total_sum - arr[-1]

    #4 find the maximum sum
    max_sum = total_sum - arr[0]

    return min_sum, max_sum


# Test example
arr = [1, 3, 5, 7, 9]
min_sum, max_sum = miniMaxSum(arr)
print(min_sum, max_sum)

