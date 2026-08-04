class Solution:
    def isValid(self, s: str) -> bool:
        # lifo
        stack = []
        matches = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for c in s:
            if c in matches:
                if not stack:
                    return False
                if stack[-1] != matches[c]:
                    return False
                stack.pop()
                continue
            stack.append(c)

        return False if stack else True