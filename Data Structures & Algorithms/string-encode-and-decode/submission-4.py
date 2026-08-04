class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        if not strs:
            return ret

        for s in strs:
            ret += str(len(s)) + ","
        ret += ";"

        for s in strs:
            ret += s

        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        if not s:
            return ret
        i = s.find(";")
        sizes = s[:i-1].split(",")
        left = i+1
        for size in sizes:
            right = left + int(size)
            ret.append(s[left:right])
            left = right
        return ret