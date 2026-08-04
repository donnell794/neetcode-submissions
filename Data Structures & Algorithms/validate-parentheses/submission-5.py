class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        d = {
            "{":"}",
            "[":"]",
            "(":")",
        }
        for c in s:
            if c in d:
                stack.append(c)
                continue
            if not stack:
                return False
            val = stack.pop()
            if c != d[val]:
                return False

        return False if stack else True