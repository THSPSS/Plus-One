class Solution:
    #my solution
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for word in words:
            if word[:len(pref)] == pref:
                 cnt += 1
        return cnt
    #other_solution
    #seems like using startwith function and send parameter
    def OtherprefixCount(self, words: List[str], pref: str) -> int:
        res=0
        for i in words:
            if i.startswith(pref):
                res+=1
        return res