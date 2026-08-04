class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        stack = []
        for c in s:
            if c not in pair:
                stack.append(c)
            else:
                if not stack or not stack[-1] == pair[c]:
                    return False
                stack.pop()

        return len(stack) == 0