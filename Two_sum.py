'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

'''
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # loop trough nums
        for i in range(len(nums)):
            find_the_number: int = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == find_the_number:
                    return [i, j]

        #brute force
        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]


        #using hash map
        #created an empty hash table to store elemnts and their indices
        hash_table = {}
        for i in range(len(nums)):
            nums[i]


        # first loop
        # from target sub the current value
        # second loop
        # from first loop number + 1 to end of the list
        # check if sub from target value is same with current looping value
        # if so save the value and break the all loop and
        # return first value and second value as list


solution = Solution()
print(solution.two_sum(nums=[3, 3], target=6))
print(solution.two_sum(nums=[15, 6, 7, 19, 2, 5], target=7))
print(solution.two_sum(nums=[0, 4, 3, 0], target=0))
print(solution.two_sum(nums=[-1, -2, -3, -4, -5], target=-8))
print(solution.two_sum(nums=[-3, 4, 3, 90], target=0))
print(solution.two_sum(nums=[3,2,95,4,-3], target=92))
#[3,2,95,4,-3]
# [-3,4,3,90]
# [-1,-2,-3,-4,-5]
