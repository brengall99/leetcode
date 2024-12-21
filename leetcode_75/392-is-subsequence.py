# https://leetcode.com/problems/is-subsequence/description/

# Two pointer solution - O(n) time complexity

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    	i, j = 0,0

    	while i < len(s) and j < len(t):
    		if s[i] == t[j]:
    			i += 1
    		j += 1

    	return True if i == len(s) else False

"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t or len(s) ==0:
            return True

        count = 0

        while True:
            for i in range(0, len(t)):
                if s[count] == t[i]:
                    count += 1
                    if count >= len(s):
                        return True
                else:
                    continue

            return False
"""