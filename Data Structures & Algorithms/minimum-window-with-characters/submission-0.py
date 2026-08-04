import string
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ""
        shortest = float('inf')
        s_dict = {}
        t_dict = {}

        for c in t:
            t_dict[c] = 1 + t_dict.get(c, 0)

        left = 0
        for right, v in enumerate(s):
            s_dict[v] = 1 + s_dict.get(v, 0)

            while self.subset(s_dict, t_dict):
                if (right - left + 1) < shortest:
                    shortest = right - left + 1
                    ret = s[left:right+1]
                
                s_dict[s[left]] -= 1
                left += 1


        return ret

    def subset(self, a, b):
        for c in b:
            if c not in a or b[c] > a[c]:
                return False

        return True