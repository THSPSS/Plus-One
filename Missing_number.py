from typing import List
def missingNumber(self , nums: List[int]) -> int:
    ##first attempt
    # for i in range(len(nums)+1):
    #     if i not in nums:
    #         return i

    #other solution
    TotalRange = len(nums)
    return TotalRange * (TotalRange + 1) // 2 - sum(nums)