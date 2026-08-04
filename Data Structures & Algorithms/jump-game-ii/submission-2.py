class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        curr_reach, max_reach = 0,0
        jump = 0

        for i in range(n):
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= n-1:
                return jump + 1

            if i == curr_reach:
                if i == max_reach:
                    return -1
                jump += 1
                curr_reach = max_reach
        return -1