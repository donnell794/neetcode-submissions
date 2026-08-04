class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        w = set()
        l = 0
        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l += 1
            w.add(s[r])
            longest = max(longest, r-l+1)

        return longest