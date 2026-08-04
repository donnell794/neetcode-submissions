class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_reach, max_reach = 0, 0
        jump = 0
        for i in range(n):
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= n-1:
                return True

            if i == curr_reach:
                if i == max_reach:
                    return False
                else:
                    jump += 1
                    curr_reach = max_reach
        return False