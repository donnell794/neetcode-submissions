class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        size = len(nums)
        ret = set()
        for i in range(size):
            for j in range(i+1, size):
                a = nums[i] + nums[j]
                if not a in d:
                    d[a] = [(i,j)]
                else:
                    d[a].append((i,j))

        for i, n in enumerate(nums):
            if -n in d:
                for j,k in d[-n]:
                    if i != j and i != k:
                        s = sorted([nums[i], nums[j], nums[k]])
                        ret.add(tuple(s))

        return [list(x) for x in ret]