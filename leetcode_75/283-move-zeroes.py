# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zero_index = 0 # pointer for position of the next non-zero element

        # move all non zero elements to the front
        for i in range(len(nums)):
            if nums [i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        # fill the remaning positions with zeros
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0


"""
Leet solution: 

left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
        return nums

-- easiest way 

for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)

The time complexity of above can be O(n^2) in the wors case, as nums.remove(nums[i]) has a time complexity of O(n) because it searches for the element and shifts the remaining elements to fill the gap.
"""