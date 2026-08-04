class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = []
        for l in range(len(temps)):
            r = l
            while r < len(temps) and temps[r] <= temps[l]:
                r += 1
            res.append(r-l if r < len(temps) else 0)
        return res