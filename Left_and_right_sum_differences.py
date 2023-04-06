from typing import List

class Solution:

    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        #using for loop/ loop through lenght of nums time
        #using slicing and sum function to make leftSum list and rightSum list

        leftSum = [sum(nums[:j]) for j in range(len(nums))]
        rightSum = [sum(nums[i+1:]) for i in range(len(nums))]

        return ([abs(x-y) for x,y in zip(leftSum , rightSum)])



    def OtherLeftRigthDifference(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            answer.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return answer