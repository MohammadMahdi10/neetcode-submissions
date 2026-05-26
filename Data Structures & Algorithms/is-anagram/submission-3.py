class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #returns true or false depending if equal or not

        if len(t) != len(s): 
            return False
        
        # we assume here that lengths are equal
        sContains = {}
        tContains = {}

        for i in range(len(s)):
            sContains[s[i]] = sContains.get(s[i], 0) + 1 #if key exists, add 1. Else, make it 0 and add
            tContains[s[i]] = tContains.get(t[i], 0) + 1

        return sContains == tContains