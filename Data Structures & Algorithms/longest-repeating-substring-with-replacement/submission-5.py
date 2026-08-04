class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        window = {}

        l=0
        max_count = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            max_count = max(max_count, window[s[r]]) 

            while (r-l+1) - max_count > k:
                window[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)
            
        return longest