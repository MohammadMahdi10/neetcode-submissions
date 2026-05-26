class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        contains = {}

        for word in strs:
            character = [0] * 26

            for letter in word:
                num = ord(letter) - ord('a')
                character[num] += 1 # += 1 not = 1 because its frequency not if it appears
            
            key = tuple(character)

            if key not in contains: # groups array indexes to words
                contains[key] = []
            contains[key].append(word)

        return list(contains.values())