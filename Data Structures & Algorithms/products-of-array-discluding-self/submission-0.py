class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # do everything before it from left side and right side the multiply

        prefix = []
        suffix = []
        both = []

        product = 1
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                product = product * nums[i-1]
                prefix.append(product)
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix.append(1)
            else:
                product = product * nums[i+1]
                suffix.append(product)
        
        
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        left = len(nums)-1
        for i in range(len(nums)):
            both.append(prefix[i]*suffix[left])
            left -= 1
        
        return both


