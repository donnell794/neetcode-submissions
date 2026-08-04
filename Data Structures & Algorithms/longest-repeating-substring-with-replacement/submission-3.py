class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        max_freq = 0
        left = 0
        for right, v in enumerate(s):
            count[v] = 1 + count.get(v, 0)
            max_freq = max(max_freq, count[v])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
            

        return res