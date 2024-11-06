# given an array of integer nums and an integer target
# return the indices of the two numbers such that they add up to target 

# you may assume that each input would have exactly one solution,
# you may not use the same element twice 

# Input: nums = [2,7,11,15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # create a dictionary to store the complements values
        complements = {}

        # iterate through the input list of numbers
        # using enumerate is better since it is clean and no need to write extra code 
        # for manual indexing, making it more readable 
        for i, num in enumerate(nums):
            # calculate the complement value needed to reach the target
            complement = target - num

            # check if the complement exists in the dictionary 
            if complement in complements:
                # if it exists, return the indices of the current number & it's complements
                return [complements[complement], i]
            
            # add the current number and its index to the dictionary 
            complements[num] = i

        # if no solution is found, return an empty list
        return []


## Find another way to solve the solution without enumerating
# Better understanding with a different example

"""
nums = [1, 3, 5, 7]
target = 8

so the goal is to add 2 numbers in nums to make 8

STEP 1: initialize with an empty hashmap 

def two_sum(self, nums, target)

    # empty hashmap here
    num_to_index = {}

First Number: 1 (at index 0)
Calculate the complement we need: 8 - 1 = 7.
Check if 7 is in num_to_index: It’s not.
Add 1 to num_to_index with its index: num_to_index = {1: 0}.

Second Number: 3 (at index 1)
Calculate the complement we need: 8 - 3 = 5.
Check if 5 is in num_to_index: It’s not.
Add 3 to num_to_index with its index: num_to_index = {1: 0, 3: 1}.

Third Number: 5 (at index 2)
Calculate the complement we need: 8 - 5 = 3.
Check if 3 is in num_to_index: It is! (Found at index 1).
Return the indices of 3 and 5: [1, 2].
So, for nums = [1, 3, 5, 7] and target = 8, the function will return [1, 2] because nums[1] + nums[2] = 3 + 5 = 8.


enumerate(iterable) takes any iterable (like a list, tuple, or string) and returns each item along with its index.
In each iteration, index is the position of the item in the iterable, and value is the item itself.

"""

nums = [10, 20, 30, 40]

for i, num in enumerate(nums):
    print(f"Index: {i}, Value: {num}")

# Index: 0, Value: 10
# Index: 1, Value: 20
# Index: 2, Value: 30
# Index: 3, Value: 40

"""
Keeps Code Clean: Instead of writing extra code to keep track of the index manually 
(e.g., using for i in range(len(nums))), enumerate does it automatically and makes the code cleaner and more readable.
Pairs Well with for Loops: When you need both the index and the value in a loop, enumerate simplifies this by unpacking them directly.
"""


