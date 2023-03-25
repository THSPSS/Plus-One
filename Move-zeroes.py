class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = 0

        is_it_has_zero = True
        while is_it_has_zero:
            if 0 in nums:
                is_it_has_zero = True
                nums.remove(0)
                zero_cnt+=1
            else:
                is_it_has_zero = False

        nums += zero_cnt * [0]
        return nums