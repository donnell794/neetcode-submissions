class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l = 0
        max_sub = 0

        for r,x in enumerate(s):
            while x in sub:
                sub.remove(s[l])
                l += 1
            sub.add(x)
            max_sub = max(max_sub, r-l+1)

        return max_sub
            