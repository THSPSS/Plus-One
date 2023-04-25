class Solution:
    def sumOfMultiples(self, n: int) -> int:
        output = 0
        a ,b ,c = 3, 5, 7
        for i in range(1,n+1):
            if i % a == 0 or i % b == 0 or i % c == 0 :
                output += i
        return output

    #using venn diagram
    def sumOfMultiples(self, n: int) -> int:
        a, b, c, d, e, f, g = n // 3, n // 5, n // 7, n // 15, n // 21, n // 35, n // 105

        return (
                       3 * a * (a + 1) +
                       5 * b * (b + 1) +
                       7 * c * (c + 1) -

                       15 * d * (d + 1) -
                       21 * e * (e + 1) -
                       35 * f * (f + 1) +

                       105 * g * (g + 1)) // 2