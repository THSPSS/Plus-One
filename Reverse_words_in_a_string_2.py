class Solution:
    #first attempt don't need to use strip 38ms
    def reverseWords(self, s: str) -> str:
        #s = s.strip()
        return ' '.join([word for word in s.split()][::-1])

    #other solution. more pythonic and took 15ms
    def OtherReverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return " ".join(s)