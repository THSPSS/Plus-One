class Solution:
    def interpret(self, command: str) -> str:
        #making parserDictionary
        parserDict = {
            'G' : 'G',
            '()' : 'o',
            '(al)': 'al'
        }
        #and making for loop through str
        #making str

    #first passed solution
    #ohter Interpret
    #more like hardcoding
    def otherInterpret(self, command: str) -> str:
        output = ""
        for i, c in enumerate(command):
            if c == "G":
                output += c
            elif c == "(" and command[i + 1] == ")":
                output += "o"
            elif c == "(" and command[i + 1] == "a":
                output += "al"
        return (output)

    #other solution using Interpreter
    #robustness
    #if add more characters it is highly changeable
    def interpret(self, s: str) -> str:
        d = {"(al)": "al", "()": "o", "G": "G"}
        tmp = ""
        res = ""
        for i in range(len(s)):
            tmp += s[i]
            if (tmp in d):
                res += d[tmp]
                tmp = ""
        return res