class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.letter_count(s) == self.letter_count(t)

    def letter_count(self, s):
        let_count = [0] * 26
        for c in s.lower():
            let_count[ord('a') - ord(c)] += 1
        return let_count