from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] == nums[j]:
                    result += 1
        return result

    #using hash map
    # search for duplicate numbers
    def otherNumIdenticalPairs(self, nums: List[int]) -> int:

        # number of good pairs
        repeat = {}
        num = 0

        # for every element in nums
        for v in nums:

            # number of repeated digits
            if v in repeat:

                # count number of pairs based on duplicate values
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]

                # increment the number of counts
                repeat[v] += 1
            # number has not been seen before
            else:
                repeat[v] = 1
        # return
        return num


    def AnotherNumIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for number in nums:
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
            else:
                hashMap[number] = 1
        return res