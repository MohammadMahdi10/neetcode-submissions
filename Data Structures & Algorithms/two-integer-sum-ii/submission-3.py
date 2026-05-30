class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = left + 1

        while left < right:
            difference = target - numbers[left]

            while numbers[right] != difference and right < len(numbers):
                right += 1
            
            if (difference) == numbers[right]:
                return [left+1, right+1]
            
            left += 1
        
        return []