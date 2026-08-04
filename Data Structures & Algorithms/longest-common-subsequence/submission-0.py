class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        cache = [[0] * (cols+1) for _ in range(rows+1)]

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if text1[r] == text2[c]:
                    cache[r][c] = 1 + cache[r + 1][c + 1]
                else:
                    cache[r][c] = max(cache[r][c + 1], cache[r + 1][c])

        return cache[0][0]