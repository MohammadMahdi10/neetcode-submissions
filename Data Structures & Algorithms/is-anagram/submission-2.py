class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sContains = {}
        tContains = {}

        for i in range(len(s)):
            if s[i] not in sContains:
                sContains[s[i]] = 1
            else:
                sContains[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in tContains:
                tContains[t[i]] = 1
            else:
                tContains[t[i]] += 1


        return sContains == tContains