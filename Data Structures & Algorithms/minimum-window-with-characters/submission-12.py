class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = [0] * ord("z")
        window_count = [0] * ord("z")

        for c in t:
            t_count[ord(c) - ord("A")] += 1

        res = [-1,float('inf')]
        l = 0
        for r in range(len(s)):
            window_count[ord(s[r]) - ord("A")] += 1

            while self.is_sub(window_count, t_count):
                res = min([res, [l,r]], key=lambda x: x[1]-x[0])
                window_count[ord(s[l]) - ord("A")] -= 1
                l += 1
                

        l,r = res
        return s[l:r+1] if r != float('inf') else ""
    
    def is_sub(self, s, t):
        return all([x >= y for x,y in zip(s,t)])