class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}

        for i in range(len(nums)):
            if nums[i] not in dictionary: #checks if the number against dictionary keys
                dictionary[nums[i]] = i #stores number : index
            else:
                return True
        
        return False

            
        