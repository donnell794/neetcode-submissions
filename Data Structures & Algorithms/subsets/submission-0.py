class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(0, nums, [], [])

    def backtrack(self, i, nums, curr_subset, uniq_subset):
        if i >= len(nums):
            uniq_subset.append(curr_subset.copy())
            return

        self.backtrack(i+1, nums, curr_subset + [nums[i]], uniq_subset)
        self.backtrack(i+1, nums, curr_subset, uniq_subset)

        return uniq_subset



        