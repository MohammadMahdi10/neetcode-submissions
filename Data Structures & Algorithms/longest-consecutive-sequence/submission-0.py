class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get minimum value
        # store the next value in the dictionary
        # check current value in dictionary
        # if not exists, then return count
        # else, increment count

        count, contains = 0, set()

        for n in nums:
            contains.add(n)
        
        for n in contains:
            start = 0
            if n-1 not in contains:
                start = n
            else:
                start = n-1
            
            if n+1 in contains:
                count += 1
        
        return count+1
