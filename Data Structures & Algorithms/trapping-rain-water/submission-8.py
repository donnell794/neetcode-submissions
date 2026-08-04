class Solution:
    def trap(self, heights: List[int]) -> int:
        max_area = 0
        l,r = 0, len(heights) - 1
        max_left = heights[l]
        max_right = heights[r]
        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, heights[l])
                max_area += max_left - heights[l]
            else:
                r -= 1
                max_right = max(max_right, heights[r])
                max_area += max_right - heights[r]

        return max_area