class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        s2_count = [0] * 26
        for i,c in enumerate(s2):
            s2_count[ord(c) - ord('a')] += 1
            if i >= len(s1):
                s2_count[ord(s2[i-len(s1)]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True

        return s1_count == s2_count
