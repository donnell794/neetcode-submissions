class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        res = 0

        for i in range(size):
            # odd
            left, right = i, i
            while left >= 0 and right < size and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            # even
            left, right = i, i+1
            while left >= 0 and right < size and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res