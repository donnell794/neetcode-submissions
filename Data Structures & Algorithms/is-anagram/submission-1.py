class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        s_count = [0]*26
        t_count = [0]*26

        for x,y in zip(s,t):
            s_count[ord(x)-ord('a')] += 1
            t_count[ord(y)-ord('a')] += 1
        return s_count == t_count