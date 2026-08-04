class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_size = 0
        size = len(s)
        for i in range(len(s)):
            # odd
            left, right = i, i
            while left >= 0 and right < size and s[left] == s[right]:
                if (right - left + 1) > res_size:
                    res_size = right - left + 1
                    res = s[left:right+1]
                left -= 1
                right += 1

            # even
            left, right = i, i+1
            while left >= 0 and right < size and s[left] == s[right]:
                if (right - left + 1) > res_size:
                    res_size = right - left + 1
                    res = s[left:right+1]
                left -= 1
                right += 1

        return res