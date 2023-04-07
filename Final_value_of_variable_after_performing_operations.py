from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if "--" in i:
                x -= 1
            else:
                x += 1
        return x

    def OtherFinalValueAfterOperations(self, operations: List[str]) -> int:
        ref = {'++X': 1, 'X++': 1, '--X': -1, 'X--': -1}
        return sum(ref[o] for o in operations)

    def OhterfinalValueAfterOperations(self, operations: List[str]) -> int:
        c = 0
        for i in operations:
            if i[1]=='+':
                c+=1
            else:
                c-=1
        return c