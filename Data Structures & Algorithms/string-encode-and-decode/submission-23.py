class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            count = len(s)
            res += str(count) + "#"
            for c in s:
                res += c

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        slen = len(s)
        l, r = 0, 0
        while r < slen:
            if s[r] == "#":
                count = int(s[l:r])
                l = r + 1
                r = l + count
                res.append(s[l:r])
                l = r
            r += 1

        return res