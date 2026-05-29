# redo this later
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get value minimum for that sequence
        # check if n+1 exists and if so, increment count
        # if sequence broken, store count in biggest
        # then go to next number and check if minimum again
        # same procedure
        # return biggest

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        contains = set()
        count, biggest = 0, 0

        for n in nums:
            contains.add(n)

        for n in contains:
            if n+1 in contains:
                count += 1
            else:
                if count > biggest:
                    biggest = count
                
                count = 0
        
        return biggest+1
            

