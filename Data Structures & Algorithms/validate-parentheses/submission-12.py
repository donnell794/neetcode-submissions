class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        stack = []
        for c in s:
            if c in m:
                if not stack or stack[-1] != m.get(c):
                    return False
                stack.pop()
            else:
                stack.append(c)
        return False if stack else True