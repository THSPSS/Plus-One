from typing import List
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    ## first_attempt
    #s.reverse()
    #return s

    #other solution
    lp, rp = 0, len(s) - 1

    while lp < rp:
        s[lp], s[rp] = s[rp], s[lp]
        lp += 1
        rp -= 1

    return s