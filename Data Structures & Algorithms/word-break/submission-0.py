class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        len_s = len(s)
        cache = [False] * (len_s+1)
        cache[len_s] = True
        for i in range(len_s-1, -1, -1):
            for w in word_dict:
                len_w = len(w)
                if i+len_w <= len_s and s[i:i+len_w] == w:
                    cache[i] = cache[i+len_w]
                if cache[i]:
                    break

        return cache[0]