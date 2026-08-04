class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        size = len(s)
        front, back = 0, size-1

        while front < back:
            if not s[front].isalnum():
                front += 1
                continue
            if not s[back].isalnum():
                back -= 1
                continue

            if s[front] != s[back]:
                return False

            front += 1
            back -= 1

        return True
            