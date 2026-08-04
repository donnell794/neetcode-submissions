class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        for s in s1:
            s1_count[ord(s) - ord("a")] += 1

        window = [0] * 26
        l,r = 0,0
        while r < len(s2):
            while r < len(s1):
                window[ord(s2[r]) - ord("a")] += 1
                r += 1

            if s1_count == window:
                return True

            if r == len(s2): break

            window[ord(s2[r]) - ord("a")] += 1
            r += 1

            window[ord(s2[l]) - ord("a")] -= 1
            l += 1
  
        return s1_count == window