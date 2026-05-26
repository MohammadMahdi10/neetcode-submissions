class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newArray = []
        for i in range(len(nums)):
            sumx = 0
            for j in range(len(nums)):
                if i >= j:
                    continue
                sumx = nums[i] + nums[j]
                if sumx == target:
                    newArray.append(i)
                    newArray.append(j)
                    newArray.sort()
                    break
        
        return newArray
