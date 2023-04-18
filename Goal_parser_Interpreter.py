class Solution:
    def interpret(self, command: str) -> str:
        #making parserDictionary
        parserDict = {
            'G' : 'G',
            '()' : 'o',
            '(al)': 'al'
        }