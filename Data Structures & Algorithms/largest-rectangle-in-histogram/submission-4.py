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

        while stack:
            h,j = stack.pop()
            max_area = max(max_area, h * (i-j+1))


        return max_area