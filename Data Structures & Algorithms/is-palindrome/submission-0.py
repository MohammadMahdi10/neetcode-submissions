class Solution:
    def isPalindrome(self, s: str) -> bool:
        # val.isalnum()
        # convert into lowercase aswell

        right = len(s)-1
        left = 0

        i = 0
        while i < len(s) and left < len(s) and right > -1:
            while s[right].isalnum() == False:
                right -= 1
            while s[left].isalnum() == False:
                left += 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            i += 1
        
        return True