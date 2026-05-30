class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = left + 1

        while left < right:
            target = target - numbers[left]
            print(target)

            while numbers[right] != target:
                right += 1
            
            if (target) == numbers[right]:
                return [left+1, right+1]
            
            left += 1
        
        return []