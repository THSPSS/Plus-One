from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #first attemp
        #ans = []
        #ans = nums * 2
        #return ans
        #other solution
        #return nums * 2

        #using Slicing and addition
        return nums+nums[:]