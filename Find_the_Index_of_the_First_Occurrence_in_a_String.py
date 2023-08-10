'''

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

'''


a = "sadbutsad"
b = "you"
class Solution:
    def find_the_index_of_the_first_occurrence_in_a_String(self, haystack , needle):
            haystack_len = len(haystack)
            needle_len = len(needle)
            return haystack.find(needle)


solution = Solution()

print(solution.find_the_index_of_the_first_occurrence_in_a_String(a , b))