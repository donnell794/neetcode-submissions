class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long, uniq = 0, set()
        l = 0
        for r in range(len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l += 1
            uniq.add(s[r])
            long = max(long, r-l+1)

        return long