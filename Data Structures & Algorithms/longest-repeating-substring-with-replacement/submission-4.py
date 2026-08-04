class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        count = {}
        max_freq = 0
        left = 0
        for right, v in enumerate(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            ret = max(ret, right - left + 1)

        return ret
            
