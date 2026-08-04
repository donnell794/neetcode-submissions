class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            let_count = tuple(self.letter_count(s))
            if let_count in group:
                group[let_count].append(s)
            else:
                group[let_count] = [s]

        return [list(x) for x in group.values()]

    def letter_count(self, s):
        let_count = [0] * 26

        for let in s:
            let_count[ord('a') - ord(let)] += 1

        return let_count