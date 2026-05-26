class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contains = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in contains:
                return [contains[complement], i]  # found the pair
            contains[num] = i  # store current num with its index
