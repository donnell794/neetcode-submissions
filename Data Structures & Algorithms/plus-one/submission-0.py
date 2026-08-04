class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = 1
        res = []
        stack = digits
        while stack:
            num = stack.pop()
            if r:
                num += 1
                r = 0
            if num == 10:
                r = 1
                num = 0
            if not stack and r:
                stack.append(r)
                r = 0
            res.append(num)
        return res[::-1]