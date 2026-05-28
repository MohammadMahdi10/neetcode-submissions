class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get minimum value
        # store the next value in the dictionary
        # check current value in dictionary
        # if not exists, then return count
        # else, increment count

        contains = set()

        biggest = 0
        current = 0

        for n in nums:
            contains.add(n)

        start = 0
        i = 0
        while i < len(contains):
            while nums[i]-1 in contains and start != nums[i]-1:
                start = nums[i]-1

            if start+1 in contains:
                current += 1
                if current > biggest:
                    biggest = current
            else:
                current = 0
            
            i+=1
        
        return biggest
