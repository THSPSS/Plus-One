from typing import List

class Solution:
    #first attempt
    #using for loop twice
    def forRestoreString(self, s: str, indices: List[int]) -> str:
        dic = {}
        output = ""

        for i in range(len(s)):
            dic[indices[i]] = s[i]

        dic = sorted(dic.items())

        for k, v in dic:
            output += v

        return (output)

    #using cnt but still not efficient
    def ctnRestoreString(self, s: str, indices: List[int]) -> str:
        dic = {}
        output = ""
        cnt = 0
        for i in indices:
            dic[i] = s[cnt]
            cnt += 1

        dic = sorted(dic.items())

        for k, v in dic:
            output += v
        return (output)

    # making empty array same length as s (string)
    # using for and zip and loop through indices and s
    # using output to join result list
    # return output
    def usingZipRestoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)
        for i, c in zip(indices, s):
            result[i] = c

        output = "".join(result)
        return (output)