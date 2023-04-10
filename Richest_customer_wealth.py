from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        #first attempt
        #using list comprehension , sum and max
        return max([sum(account) for account in accounts])

        return max(map(sum, accounts))