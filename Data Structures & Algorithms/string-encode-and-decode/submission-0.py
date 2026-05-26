class Solution:

    def encode(self, strs: List[str]) -> str:
        concatenate = ""
        for s in strs:
            concatenate += str(len(s)) + "#"
            for c in s:
                concatenate += str(ord(c)) + ","

        return concatenate

    def decode(self, s: str) -> List[str]:
        pos = 0
        result = []

        while pos < len(s):
            length = 0
            st = ""
            while s[pos] != "#":
                st += s[pos]
                pos += 1
            length = int(st)
            pos += 1
            
            current_word = ""
            for i in range(length):
                numStr = ""
                while s[pos] != ",":
                    numStr += s[pos]
                    pos += 1
                current_word += chr(int(numStr))
                pos += 1

            result.append(current_word)
        
        return result
