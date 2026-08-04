class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        d = defaultdict(list)
        v = set()
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if (j,i) in v:
                    continue
                d[nums[i]+nums[j]].append([i,j])
                v.add((j,i))

        res = set()
        for i in range(l):
            if 0-nums[i] in d:
                for pair in d[0-nums[i]]:
                    if i not in pair:
                        res.add(tuple(sorted([nums[i],*[nums[x] for x in pair]])))
        return [list(li) for li in res]