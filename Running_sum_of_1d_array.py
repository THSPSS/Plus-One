from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #my solution
        return ([sum(nums[:i+1]) for i in range(len(nums)) ])

        #other solution
    def otherRunningSum(self, nums: List[int]) -> List[int]:
        running_sum = []

        current_sum = 0

        for num in nums:
            current_sum += num

            running_sum.append(current_sum)

        return running_sum

      #fastest running time 16ms
        def runningSum(self, nums: List[int]) -> List[int]:
            ret = [nums[0]]
            for v in nums[1:]:
                ret.append(ret[-1] + v)
            return ret
