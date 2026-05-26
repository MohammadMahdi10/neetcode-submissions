class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #num i + num j = target
        #we can also do target - num i = num j

        sums = {}

        for i in range(len(nums)):
            sums[nums[i]] = i
        
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in sums and sums[difference] != i:
                return [i, sums[difference]]