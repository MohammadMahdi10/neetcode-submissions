class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contains = {} 

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in contains:
                return [contains[compliment], i]
            contains[nums[i]] = i