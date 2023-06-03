# Staircase takes a integer to make a staircase shape 
# #
# ##
# ###
# ####

def staircase(n):
    for i in range(1, n+1):
        print(' '*(n-i) + '#'*i)

staircase(6)