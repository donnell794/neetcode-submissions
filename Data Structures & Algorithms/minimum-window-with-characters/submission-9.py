class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t:
            return ""

        t_count = [0] * 122
        for c in t:
            t_count[ord(c) - ord('A')] += 1

        res, res_len = [-1,-1], float('inf')
        s_count = [0] * 122
        l,r = 0,0
        while r < len(s):
            s_count[ord(s[r]) - ord('A')] += 1
            while self.is_sub(s_count, t_count):
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1               
                s_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            r += 1

        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""

    
    def is_sub(self, s, t):
        return all([x >= y for x,y in zip(s,t)])