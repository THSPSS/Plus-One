'''

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

'''


a = "mississippi"
b = "sad"
class Solution:
    def find_the_index_of_the_first_occurrence_in_a_String(self, haystack , needle):
            answer = -1
            haystack_len = len(haystack)
            needle_len = len(needle)
            for i in range(haystack_len):
                print(f"print {haystack[i:i+needle_len]}")
                if haystack[i:i+needle_len] == needle :
                    answer = i
            return answer

            #return haystack.find(needle)


solution = Solution()

print(solution.find_the_index_of_the_first_occurrence_in_a_String(a , b))