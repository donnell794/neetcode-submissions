class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sub = [0] * 26
        s2_sub = [0] * 26
        k = len(s1)
        for s in s1:
            s1_sub[ord(s) - ord('a')] += 1

        for i, s in enumerate(s2):
            s2_sub[ord(s) - ord('a')] += 1
            if i >= k:
                s2_sub[ord(s2[i-k]) - ord('a')] -= 1
            if s1_sub == s2_sub:
                return True

        return s1_sub == s2_sub

