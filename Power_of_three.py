#first attemp : it was not good at all.
#it is long and confusing
#and fail at 45 it return true/ otherwise it should be false
def isPowerOfThree(self, n: int) -> bool:
    if n <= 0:
        return False

    else:

        not_find_power_three_result = True
        result = "False"
        three, power = 3, 1
        while not_find_power_three_result:
            comparing_num = pow(three, power)
            if comparing_num == n:
                result = "True"
                return result
            elif comparing_num < n < pow(three, power + 1):
                not_find_power_three_result = False
                return result
            else:
                power += 1


#others solution
#much simple and clean code
#while throw nums until it is less than given number , n
#while loop num multiply num
#check if result of num is ams whith n
class Solution:
    def otherSolutionIsPowerOfThree(self, n: int) -> bool:
        num = 1
        while num < n:
            num *= 3
        return num == n
