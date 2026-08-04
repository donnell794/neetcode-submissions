class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        size = len(s)
        res = []

        while i < size:
            j = i
            while j < size and s[j] != "#":
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            res.append(s[i:j])

            i=j
        return res