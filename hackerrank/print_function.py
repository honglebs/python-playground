# Print numbers n 
# n = 3
# print 1 2 3

def printNumbers(n):
    numbers_list = []
    for i in range(1, n + 1):
        numbers_list.append(str(i))
    return ''.join(numbers_list)

print(printNumbers(3))