class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache
        cache = [[0] * (n+1) for _ in range(m+1)]
        #base case
        cache[m-1][n-1] = 1
        # bottom-up
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                cache[r][c] += cache[r+1][c] + cache[r][c+1]

        return cache[0][0]