class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            min_h = heights[i]
            for j in range(i, len(heights)):
                min_h = min(min_h, heights[j])
                max_area = max(max_area, min_h * (j-i+1))

        return max_area