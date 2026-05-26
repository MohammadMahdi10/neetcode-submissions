class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray = []
        tArray = []
        
        for i in range(len(s)):
            sArray.append(s[i])
        for i in range(len(t)):
            tArray.append(t[i])

        tArray.sort()
        sArray.sort()

        return tArray == sArray
        