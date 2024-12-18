# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        f = [0] + flowerbed + [0] # add extra 0's to allow us to deal with edge cases, for example: [0, 0, 1]

        for i in range(1, len(f) - 1): # iterate between original flowerbed
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0: # check prev, i, and next spaces
                f[i] = 1 # plant a flower if true
                n -= 1 # decrement n

        return n <= 0 