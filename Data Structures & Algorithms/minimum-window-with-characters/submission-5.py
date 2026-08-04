class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = [-1,-1]
        ret_size = float('inf')
        window, t_dict, = {}, {}

        for c in t:
            t_dict[c] = 1 + t_dict.get(c, 0)

        have = 0
        need = len(t_dict)
        left = 0

        for right, v in enumerate(s):
            window[v] = 1 + window.get(v, 0)
            if v in t_dict and window[v] == t_dict[v]:
                have += 1

            while have == need:
                if right - left + 1 < ret_size:
                    ret = [left, right]
                    ret_size = right - left + 1

                window[s[left]] -= 1
                if s[left] in t_dict and window[s[left]] < t_dict[s[left]]:
                    have -= 1
                
                left += 1

        left, right = ret
        return s[left:right+1] if ret_size != float('inf') else ""