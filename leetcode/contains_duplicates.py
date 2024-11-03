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

# Approach 2: Sorting 

# Approach 3: Hashset 

# Approach 4: Hashmap

#===================================================================

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



