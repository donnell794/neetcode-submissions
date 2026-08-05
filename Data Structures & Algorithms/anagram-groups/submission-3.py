class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            s_count = self.c_count(s)
            if s_count not in group:
                group[s_count] = []
            group[s_count].append(s)

        return [x for x in group.values()]
            
    
    def c_count(self, s):
        c_count = [0] * 26

        for c in s:
            c_count[ord(c) - ord("a")] += 1

        return tuple(c_count)