class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []
        for i in range(len(temps)):
            while stack and stack[-1][0] < temps[i]:
                t,j = stack.pop()
                res[j] = i-j

            stack.append((temps[i], i))

        return res