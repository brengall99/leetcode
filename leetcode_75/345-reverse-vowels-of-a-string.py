# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Use a set for faster lookup
        s = list(s)  # Convert string to a list for mutability

        left, right = 0, len(s) - 1  # Two pointers

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                # Swap vowels
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)  # Convert list back to string