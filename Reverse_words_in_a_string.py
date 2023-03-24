class Solution:
    #my solution 38ms
    def reverseWords(self, s: str) -> str:
        newString = ' '.join([word[::-1] for word in s.split()])

        return newString

    #other solution runtime 15ms
    def OtherSolutionReverseWords(self, s: str) -> str:
        s_list = s.split()
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
        return ' '.join(s_list)