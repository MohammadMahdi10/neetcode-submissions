class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get minimum value
        # store the next value in the dictionary
        # check current value in dictionary
        # if not exists, then return count
        # else, increment count

        if len(nums) == 0:
            return 0

        contains = set()

        biggest = 0
        current = 0

        for n in nums:
            contains.add(n)
        
        for n in contains:
            if n+1 in contains:
                current += 1
                if current > biggest:
                    biggest = current
            else:
                current = 0
        
        return biggest+1
