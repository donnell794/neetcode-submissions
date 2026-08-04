class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        first = 0
        second = len(lower_s)-1
        while first < second:
            left = lower_s[first]
            right = lower_s[second]
            if not left.isalnum():
                first += 1
                continue
            if not right.isalnum():
                second -= 1
                continue
            if left != right:
                return False
            first += 1
            second -= 1

        return True
        