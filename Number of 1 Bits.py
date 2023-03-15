class Solution:
    def hammingWeight(self, n: int) -> int:
        string_n = bin(n)
        solution = string_n.count("1")
        return int(solution)

        # return int(bin(n).count("1"))



solution = Solution()

answer = solution.hammingWeight(0o000000000000001101)

print(answer)