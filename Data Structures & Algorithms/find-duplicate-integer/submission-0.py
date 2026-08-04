class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        fast, slow = 0,0

        while 1:
            fast += 2
            slow += 1

            if fast >= size:
                fast = fast - size

            if slow >= size:
                slow = slow - size

            if nums[fast] == nums[slow]:
                return nums[slow]