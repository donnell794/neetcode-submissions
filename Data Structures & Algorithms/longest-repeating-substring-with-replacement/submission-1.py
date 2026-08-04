class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        max_freq = 0
        left = 0
        longest = 0
        freq = [0] * 26

        for right in range(size):
            c=ord(s[right]) - ord('A')
            freq[c] += 1
            max_freq = max(max_freq, freq[c])

            while (right-left+1) - max_freq > k:
                c=ord(s[left]) - ord('A')
                freq[c] -= 1    
                left += 1

            longest = max(longest, right-left+1)


        return longest