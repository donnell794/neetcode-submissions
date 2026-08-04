class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        cache = {size:1}
        for i in range(size-1, -1, -1):
            if s[i] == "0":
                cache[i] = 0
            else:
                cache[i] = cache[i+1]
            if i+1 < size and (s[i] == "1" or 
                s[i] == "2" and s[i+1] in "0123456"
            ):
                cache[i] += cache[i+2]

        return cache[0]