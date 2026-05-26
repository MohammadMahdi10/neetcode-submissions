class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        count = 0

        for s in nums:
            if s in output:
                output[s] += 1
            else:
                output[s] = 1

        sorted_items = sorted(output.items(), key=lambda x: x[1], reverse=True)
        outputA = []
        for i in range(k):
            outputA.append(sorted_items[i][0])
        
        return outputA




        