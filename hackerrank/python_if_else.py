
# Pythong If Else Practice 

# Given an integer, n, perform the following conditional actions:

# If is odd, print "Weird"
# If is even and in the inclusive range of 2 to 5, print "Not Weird"
# If is even and in the inclusive range of 6 to 20, print "Weird"
# If is even and greater than 20, print "Not Weird"



def werido(n):

    # check if n is odd using mod
    if n % 2 == 1:
        print ("Weird")

    # check if n is even & in range [2, 5]
    elif n >= 2 and n <= 5:
        print("Not weird")

    # check if n is even & in range [6, 20]
    elif n >=6 and n <= 20:
        print("Weird")

    # if even and greater than 20
    else:
        print("Not Werid")

print(werido(24))
    
    

