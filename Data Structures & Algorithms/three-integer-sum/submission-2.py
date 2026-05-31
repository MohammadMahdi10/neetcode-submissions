class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i + j + k = 0 -> -i= k + j
        # iterate through i and check if -i = k + j via two pointers

        val = sorted(nums)
        collect = []

        for i in range(len(val)):
            if i>0:
                if val[i] == val[i-1]:
                    continue

            jP = i+1
            kP = len(val)-1

            target = -val[i]

            while jP < kP:
                if target == val[jP] + val[kP]:
                    collect.append([val[i], val[jP], val[kP]])
                    jP += 1

                    while nums[jP] == nums[jP - 1] and jP < kP:
                        jP += 1


                elif val[jP] + val[kP] < target:
                    jP += 1
                else:
                    kP -= 1

        return collect

            