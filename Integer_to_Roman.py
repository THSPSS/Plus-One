'''
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:


Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''


class Solution:
    #Constratins number
    #1 <= num <= 3999
    def intToRoman(self, num: int) -> str:
        hash_map = {
             1 :  "I",
             5 :  "V",
             10:  "X",
             50:  "L",
             100: "C",
             500: "D",
            1000: "M",
        }
        #check number
        #check if number is smaller than other
        #each number divide with each section
        #divde number with each digit
        #1000  , 500 , 100 , 50 , 10 , 5 , 1
        count = 0
        for i in range(len(num)):
            count += 1
            print(num / 1000)
            result = num / 1
            #multiply "M" three times



        return



solution = Solution()
print(solution.intToRoman(3999))
