class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            for c in s:
                encoded += f"{ord(c)}#"
            encoded += ";"
        encoded += "$"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        first=0
        last=first
        
        while s[last] != "$":
            if s[first] == ";":
                temp = ""
                for c in s[last:first].split("#"):
                    temp += chr(int(c)) if c else ""
                decoded.append(temp)
                last = first+1

            first += 1

        return decoded