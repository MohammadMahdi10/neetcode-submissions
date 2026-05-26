class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left = 0
        right = left + 1
        length = len(nums)

        while left < length - 1:
            if right >= length:
                left += 1
                right = left + 1
                continue
            
            if nums[left] == nums[right]:
                return True
            
            right += 1
        
        return False
        