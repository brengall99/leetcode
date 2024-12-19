# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        parts = s.split()
        reverse_list = parts[::-1]
        return ' '.join(reverse_list)

solution = Solution()
result = solution.reverseWords("the sky is blue")
print(result)