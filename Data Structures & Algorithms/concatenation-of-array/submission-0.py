class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(2):
            for n in nums:
                x.append(n)

        return x;