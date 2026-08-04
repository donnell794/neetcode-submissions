class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            c_list = self.char_list(s)
            if anagrams.get(c_list):
                anagrams[c_list].append(s)
            else:
                anagrams[c_list] = [s]

        return anagrams.values()

    def char_list(self, s):
        chars = [0]*26
        for c in s:
            chars[ord(c) - ord('a')] += 1
        return tuple(chars)