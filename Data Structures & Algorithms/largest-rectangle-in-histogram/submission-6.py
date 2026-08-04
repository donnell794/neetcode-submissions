class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                h,j = stack.pop()
                max_area = max(max_area, h * (i-j))
                start = j
            stack.append((heights[i], start))

        n = len(heights)
        while stack:
            h,j = stack.pop()
            max_area = max(max_area, h * (n-j))

        return max_area