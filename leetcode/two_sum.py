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

STEP 2: iterate though nums

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

"""
Walkthrough of Finding Complements
First Number: 1

Complement Calculation: 8 - 1 = 7
Interpretation: To get a sum of 8 with 1, we need to find a 7 somewhere in nums.
Since 7 hasn’t been seen yet, we add 1 to our hashmap.
Second Number: 3

Complement Calculation: 8 - 3 = 5
Interpretation: To get a sum of 8 with 3, we need to find a 5 in nums.
Since 5 hasn’t been seen yet, we add 3 to our hashmap.
Third Number: 5

Complement Calculation: 8 - 5 = 3
Interpretation: To get a sum of 8 with 5, we need to find a 3 in nums.
Result: 3 is already in our hashmap (we saw it at index 1). This means that 5 and 3 together add up to 8, so we can return [1, 2].
Why Does This Work?
By calculating target - num, we’re essentially figuring out the exact number we’d need to reach target when combined with num.

When we check if the complement exists in the hashmap, it tells us if we’ve already seen this "partner" number earlier in the list. If so, we’ve found our solution, because the current number and the complement together will equal the target.

Visualization with the Example
Here’s a visualization of what’s happening in each iteration:

Index	Number	Complement Needed	HashMap	            Match Found?
0	    1	    7	                {1: 0}	            No
1	    3	    5	                {1: 0, 3: 1}	    No
2	    5	    3	                {1: 0, 3: 1, 5: 2}	Yes!

When we reach 5 at index 2, we look for 3 in the hashmap and find it. This tells us that 3 and 5 together add up to 8.

Time complexity: looping through nums is O(n) since we are looping each number and linear
                hashmap operations is O(1) we were are checking map or adding to it --> O(n)
Space complexity: In the worst case, we may need to store all n elements in the hashmap 
                (if we don’t find a solution until the very end of the list). So the space complexity is also O(n).
"""


#======================================================================================================
#======================================================================================================
#======================================================================================================

# this is not the best solution, since it takes two nested loops and compare every possible pair of elements 


def two_sum_brute_force(nums, target):

    # loop through each element in the list
    for i in range(len(nums)):

        # for each element, loop through the next elements in the list
        for j in range(i + 1, len(nums)):

            # check if the sum of nums[i] and nums[j] equals the target 
            if nums[i] + nums[j] == target:
                return [i, j]
            
    # if no solution is found, return an empty list 
    return []

"""
Let’s say nums = [1, 3, 5, 7] and target = 8:

Outer Loop (i = 0, nums[i] = 1):
Inner Loop (j = 1, nums[j] = 3): 1 + 3 is not 8.
Inner Loop (j = 2, nums[j] = 5): 1 + 5 is not 8.
Inner Loop (j = 3, nums[j] = 7): 1 + 7 is 8, so we return [0, 3].
The function stops as soon as it finds the correct indices, [0, 3].
"""


