class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        max_area = 0

        for left, n in enumerate(heights):
            for right in range(left, size):
                area = (right-left) * min(n, heights[right])
                max_area = max(max_area, area)

        return max_area
