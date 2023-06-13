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
