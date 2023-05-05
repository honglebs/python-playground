# Strong Password

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
# the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

# Its length is at least 6.
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@  # $%^&*()-+

# GIVEN IN PROBLEM #
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# ====== NOTES ====== #

# def minimumNumber(n, password):
#     # Return the minimum number of characters to make the password strong
    
#     count = 0

#     if not any (char.isdigit() for char in password):
#         count += 1
    
#     if not any (char.islower() for char in password):
#         count += 1
    
#     if not any (char.isupper() for char in password):
#         count += 1
    
#     if not any (char in special_characters for char in password):
#         count += 1
    
#     if n < 6:
#         count += 6 - n

#     return count


def minimumNumber(n, password):
    return None