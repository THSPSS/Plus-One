
'''

loop through hours List and compare each element with target

if element is same or bigger than target number , than count up


and after loop through list return cnt value


'''


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0
        for i in hours:
            if i >= target:
                cnt += 1

        return cnt