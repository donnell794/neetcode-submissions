class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        long, window = 0, {}

        l, count = 0, 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            count = max(count, window[s[r]])
            
            while (r-l+1) - count > k:
                window[s[l]] -= 1
                l += 1

            long = max(long, r-l+1)
            
        return long