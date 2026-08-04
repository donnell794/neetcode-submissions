class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        chars = defaultdict(list)
        for s in strs:
            char = self.to_char(s)
            chars[char].append(s)

        return [l for l in chars.values()]
    def to_char(self, s):
        chars = [0] * 26

        for c in s:
            chars[ord('a')-ord(c)] += 1

        return tuple(chars)