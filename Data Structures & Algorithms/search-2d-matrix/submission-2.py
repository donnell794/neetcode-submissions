class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            if matrix[r][0] == target:
                return True
            if matrix[r][0] >= target:
                r -= 1
                break
        for c in range(len(matrix[r])):
            if matrix[r][c] == target:
                return True

        return False