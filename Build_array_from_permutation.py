from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #first attemp
        # ans = []
        # for i in nums:
        #     ans.append(nums[i])
        # return ans
        # other solution
        return [nums[nums[i]] for i in range(len(nums))]