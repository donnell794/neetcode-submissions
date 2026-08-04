class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        max_sub = 0
        
        left = 0

        for left in range(size):
            substr = set()
            right = left
            while right < size:
                if s[right] in substr:
                    break
                substr.add(s[right])
                right += 1

            max_sub = max(max_sub, right - left)

        return max_sub