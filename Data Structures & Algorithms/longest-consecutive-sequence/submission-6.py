class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        visited = set()
        longest = 0
        size = len(nums)

        for  n in nums:
            if n in visited:
                continue
            
            t = n
            l = 0
            while t in s:
                visited.add(t)
                l += 1
                t += 1
            longest = max(longest, l)

        return longest