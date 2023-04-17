from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            num = nums[i]
            count = 0
            for j in range(len(nums)):
                if num > nums[j] :
                    count += 1
            output.append(count)
        return (output)

    def ohterSmallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        mapping = dict()
        for i, n in enumerate(sorted_nums):
            if n not in mapping:
                mapping[n] = i

        return [mapping[key] for key in nums]