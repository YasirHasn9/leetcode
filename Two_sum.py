# Given an array of integers, return indices of the two
# numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Example:

def twoSum(nums, target):
    '''
        arr of integers , num
        output ---> indexes of 2 intergers == target
    '''
    r = {}
    for i, val in enumerate(nums):
        remained = target - val
        if remained in r:
            return [r[remained], i]
        r[val] = i
    return []


nums = [2, 7, 11, 15]
print(twoSum(nums, 9))
