# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)
        left, right = 1, 1

        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
            output[len(nums)-i-1] *= right
            right = right*nums[len(nums)-i-1]

        return output