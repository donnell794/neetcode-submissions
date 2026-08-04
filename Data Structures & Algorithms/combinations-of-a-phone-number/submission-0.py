class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        keypad = {
            # '1' : ['.', ',', '?', '!', ':'],
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
            # '0' : [' ']
        }
        
        return self.backtrack(0, digits, "", [], keypad)

    def backtrack(self, i, digits, curr, combos, keypad):
        if i >= len(digits):
            combos.append(curr)
            return

        for d in keypad.get(digits[i]):
            self.backtrack(i+1, digits, curr + d, combos, keypad)

        return combos