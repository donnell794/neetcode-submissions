class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i,h in enumerate(heights):
            for j in range(i, len(heights)):
                min_h = min(h,heights[j])
                max_area = max(max_area, min_h*(j-i))

        return max_area