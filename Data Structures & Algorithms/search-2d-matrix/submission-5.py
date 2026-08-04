class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) - 1
        for r in range(len(matrix)):
            if matrix[r][n] >= target:
                return self.binary_search(matrix[r], target)
        return False
        
    def binary_search(self, arr, target):
        l,r = 0, len(arr)-1
        while l <= r:
            mid = (l + r) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False