class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = []

        for i in range(size):
            j=i+1
            while j < size and temperatures[j] <= temperatures[i]:
                j += 1
            res.append(j-i if j < size else 0)
        return res