# Staircase takes a integer to make a staircase shape 
# #
# ##
# ###
# ####

# i still do not undersyand this algo

def staircase(n):
    for i in range(1, n+1):
        print(' '*(n-i) + '#'*i)

staircase(6)