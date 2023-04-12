class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # my solution
        #using while loop and if statement
        #it it too long and do not need to use while statement
        num = 1
        while n * num <= n*2:
            if n*num % 2 == 0:
                return n*num
            num += 1

     #ohter solution
     # if n is even number than return n
     # else (if it is odd number) than return n * 2

    def otherSmallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n * 2

    #using Bit solution
    def bitSmallestEvenMultiple(self, n):
        return n << (n & 1)