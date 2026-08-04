class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums_len = len(nums)

        def dfs(i, combs, total):
            if total == target:
                res.append(combs.copy())
                return
            if i >= nums_len or total > target:
                return

            dfs(i, combs + [nums[i]], total + nums[i])
            dfs(i+1, combs, total)

        dfs(0,[],0)
        return res