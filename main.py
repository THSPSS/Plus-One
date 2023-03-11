class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9 :
            digits[-1] += 1
            return digits
        else :
            new_integer = int(''.join(map(str, digits)))
            new_integer += 1
            new_integer = map(int, str(new_integer))
            return new_integer

