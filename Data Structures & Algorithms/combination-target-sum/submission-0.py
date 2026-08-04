class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        uniq = self.backtrack(nums, target, [], set())
        return [list(u) for u in uniq]

    def backtrack(self, nums, target, curr, uniq):
        if sum(curr) == target:
            curr.sort()
            uniq.add(tuple(curr))
        
        if sum(curr) > target:
            return

        for n in nums:
            self.backtrack(nums, target, curr + [n], uniq)

        return uniq
        
    