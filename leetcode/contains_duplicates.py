"""
# Given an integer array nums, return ture if any value appears at least twice in the array
# and return false if every element is distinct 

# Example 1:
    input: nums = [1, 2, 3, 1]
    output: true

# Example 2:
    input: nums = [1, 2, 3, 4]
    output: false

# Example 3:
    input: nums = [1,1,1,3,3,4,3,2,4,2]
    output: true

"""

# Approach 1: Brute Force
# aka, the worst one since the time complexitity is O(n^2) --> uses nested loops to generate and all pairs possible
class SolutionBruteForce: 
    def containsDuplicate(self, nums):
        n = len(nums)

        for i in range (n - 1):
            for j in range (i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


# Approach 2: Sorting 
# sorting the array in ascending order and then checks for adjacent elements that are the same
# if duplicates are found, returns true, approach is O(n log n) 
class SolutionSorting: 
    def containsDuplicates(self, nums):
        nums.sort()
        n = len(nums)

        for i in range (1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


# Approach 3: Hashset 
# uses the hash set data structure to store encountered elements 
class SolutionHashSet:
    def containsDups(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Approach 4: Hashmap
# this is similar to hash set but it also keep track of the count of occurrences for each
# element, store the elements as keys and thier counts as values
class SolutionHashMap:
    def containsDuplicates2(self, nums):
        seen = {}

        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False


#======================================================================================================
#======================================================================================================
#======================================================================================================

class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on.')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off.')
        else:
            print(f'Microwave ({self.brand}) is already turned off.')
            
    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print(f'A mystical force whisphers: "Turn on your microwavw first..."') 


smeg: Microwave = Microwave('Smeg', 'B')

smeg.turn_on()
smeg.turn_on()

# bosch: Microwave = Microwave('Bosch', 'C')
# print(bosch)
# print(bosch.brand)
# print(bosch.power_rating)



