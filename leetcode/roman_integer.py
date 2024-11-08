# Roman numerals are represented by seven differnt symbols: I, V, X, L, C, D, M
# VI would be six


"""
====================================================================================
SYMBOL     VALUE 
I           1
V           5
X           10
L           50
C           100
D           500
M           1000
====================================================================================

so, we need to understand that there are key rules for roman numerals
1. Additive Rule -- symboles are generally added together 
    VI -> 5 + 1 = 6
    XIII -> 10 + 1 + 1 + 1 = 13

2. Subtractive Rule -- when a smaller numeral appears before a larger one, it is subtacted
    IV -> 5 - 1 = 4
    IX -> 10 -1 = 9
    XL -> 50 - 10 = 40




"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

    # creating a look up table to store the roman numerals
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }


