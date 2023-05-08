# Compare the Triplets

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# ======= NOTES =======#
# a = [1, 2, 3]
# b = [3, 2, 1]
# For elements * 0*, Bob is awarded a point because a[0] .
# For the equal elements a[1] and b[1], no points are earned.
# Finally, for elements 2, a[2] > b[2] so Alice receives a point.
# The return array is [1, 1] with Alice's score first and Bob's second.

def compareTriplets(a, b):

    # init a score for both alice and bob to count how many points they get
    scoreA = 0
    scoreB = 0

    # iterate through the triplet range of 3
    for i in range (3):

        # condition if a is bigger, add a point to alice
        if a[i] > b[i]:
            scoreA += 1
        
        # 2nd conidition, if b is bigger, add point to bob
        elif a[i] < b[i]:
            scoreB += 1
    
    # returing the scores in an array [alice, bob]
    return [scoreA, scoreB]

print(compareTriplets([1, 2, 3], [3, 2, 1]))
print(compareTriplets([4, 3, 2], [6, 3, 1]))