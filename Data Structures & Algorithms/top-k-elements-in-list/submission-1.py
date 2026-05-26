class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        contains = []

        for n in nums:
            if n not in frequencies:
                frequencies[n] = 0
            frequencies[n] += 1
        
        sortedItems = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            contains.append(sortedItems[i][0])


        return contains