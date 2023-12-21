'''

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        # make a hash map ?
        # or using switch or if to convert roman to integer?
        # from left to right , largest to the smallest one
        # if left one is smaller than right one than substract from right one to left one and get number
        # making list or hash map with string and make it each letter as key , but if letter and after that letter is bigger than letter
        # than make that two substract it
        hash_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        for i in range(len(s)):
            if i != len(s)-1 and hash_map[s[i]] < hash_map[s[i+1]]:
                #result += hash_map[s[i+1]] - hash_map[s[i]]
                result -= hash_map[s[i]]
            else:
                result += hash_map[s[i]]

        return result


    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number



solution = Solution()
print(solution.romanToInt("XIV")) #14
print(solution.romanToInt("CXL")) #140
print(solution.romanToInt("III")) #3
print(solution.romanToInt("LVIII")) #58
print(solution.romanToInt("MCMXCIV")) #1994