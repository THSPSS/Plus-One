'''
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.
'''
from typing import List
class Solution:
    #using Insert
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        new_list = []
        for n , i in zip(nums, index):
            new_list.insert(i ,n)
        return (new_list)
    #without using Insert
    def otherCeateTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for n, i in zip(nums, index):
            arr[i:i] = [n]
        return arr
