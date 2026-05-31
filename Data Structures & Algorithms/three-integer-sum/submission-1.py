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
                    arr = []

                    arr.append(val[i])
                    arr.append(val[jP])
                    arr.append(val[kP])
                    collect.append(arr)

                    jP += 1
                    kP -= 1

                elif val[jP] + val[kP] < target:
                    jP += 1
                else:
                    kP -= 1

        return collect

            