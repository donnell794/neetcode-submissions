class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        longest = 0
        left = 0
        for right, v in enumerate(s):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.add(s[right])
            longest = max(longest, len(sub))

        return longest
