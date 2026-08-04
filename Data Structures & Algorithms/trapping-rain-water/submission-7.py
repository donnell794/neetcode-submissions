class Solution:
    def trap(self, heights: List[int]) -> int:
        max_area = 0
        size = len(heights)
        max_left = [heights[0]]
        max_right = [heights[-1]]
        for i in range(1, size):
            max_left.append(max(max_left[-1], heights[i]))

        for i in range(size-2, -1, -1):
            max_right.append(max(max_right[-1], heights[i]))
        
        for i in range(size):
            min_h = min(max_left[i], max_right[size-i-1])
            area = min_h - heights[i]
            max_area += area if area else 0 

        return max_area