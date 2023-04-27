'''
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.

'''


class Solution:
    def countDigits(self, num: int) -> int:
        output = 0
        for i in str(num) :
            if num % int(i) == 0:
                output += 1
        return output