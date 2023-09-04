'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.


check min string from each word
and loop through word from start
if first word of each word is not same
then return empty string
otherwise compare all word from start until there is different

'''

'''
check first word and if first word is not same than it has not have prefix
which return emtpy string like this ""
if all words had same first word than move on to next word

so it does not have to be all words. pick any word and start it

in this case first index word can be fine

'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        least_num = None
        list_min = min([len(i) for i in strs])
        print(f"list_min {list_min}")
        # loop through each vocabs with for loop (with min string from words)
        # it only return the first word
        for num in range(list_min):
            print(strs[0][num])
            string += strs[0][num]
            print(f"string after add str[0][num] {string}")
            for i in range(1 , len(strs)):
                print(f"element {strs[i]}")
                if strs[i][0] != string:
                    string = ""
                    return string
                    break
                if not strs[i].startswith(string):
                    least_num = num - 1

        return strs[0][0:least_num]


solution = Solution()

strs = ["flower", "flow", "flight"]
answer = solution.longestCommonPrefix(strs)
print(f"this is answer {answer}")
