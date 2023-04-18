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
    def otherInterpret(self, command: str) -> str:
        output = ""
        for i, c in enumerate(command):
            if c == "G":
                output += c
            if c == "(" and command[i + 1] == ")":
                output += "o"
            if c == "(" and command[i + 1] == "a":
                output += "al"
        return (output)