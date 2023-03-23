class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1

        #other solution
        while n > 0:
            d = n % 10
            s += d
            p *= d
            n = n // 10

        # first attemp
        # for d in str(n):
        #     d = int(d)
        #     s += d
        #     p *= d

        return (p - s)
