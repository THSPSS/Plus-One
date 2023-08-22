'''

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


other solution

Intuition:
The intuition behind this approach is that if an element occurs more than n/2 times in the array (where n is the size of the array), it will always occupy the middle position when the array is sorted. Therefore, we can sort the array and return the element at index n/2.

Explanation:
The code begins by sorting the array nums in non-decreasing order using the sort function from the C++ Standard Library. This rearranges the elements such that identical elements are grouped together.
Once the array is sorted, the majority element will always be present at index n/2, where n is the size of the array.
This is because the majority element occurs more than n/2 times, and when the array is sorted, it will occupy the middle position.
The code returns the element at index n/2 as the majority element.

'''
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums) / 2
        unique_values = []
        for x in nums:
            if x not in unique_values:
                unique_values.append(x)

        for j in unique_values:
            if nums.count(j) > limit:
                return j

    def ohterSolutionMajorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n // 2]

    def hashMapSolution(self, nums: List[int]) -> int:
        nums_len = len(nums)
        m = {}

        for number in nums:
            if number in m:
                m[number] += 1
            else:
                m[number] = 1

        nums_len //= 2
        for k, v in m.items():
            if v > nums_len:
                return k


'''
Approach 2: Hash Map
using defaultDictionary with key and value
'''




