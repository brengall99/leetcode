# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution(object):
    def kidsWithCandies(self, candies: list, extraCandies: int) -> List[bool]:
        
        result = []
        
        for candy in candies:
            if candy + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        
        return result