class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = self.str_count(s)
        t_count = self.str_count(t)

        return s_count == t_count


    
    def str_count(self, s):
        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - ord('a')] += 1

        return char_count