from typing import List

#my brute solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(0, len(nums)):
                if nums[i] == target:
                   return i
        else:
            for i in range(0 , len(nums)):
                if i == 0 and nums[i] > target:
                        return i
                if i < len(nums)-1:
                    if nums[i] < target < nums[i+1]:
                        return i+1
                else:
                    return i+1


#ohter solution runtime 27ms
class OtherSolution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                end = mid - 1

            else:
                start = mid + 1

        return start

#ohter solution memory 14.8MB
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m
            else:
                r = m - 1
        return l