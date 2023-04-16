from typing import List

class Solution:
    #my solution
    def mostWordsFound(self, sentences: List[str]) -> int:
        for i in range(len(sentences)):
            sentences[i] = len(sentences[i].split(' '))
        return max(sentences)

    #other solution
    '''
    Count spaces in each sentence, and return max + 1. 
    The benefit (comparing to a split method) is that we do not create temporary strings.
    '''
    def otherMostWordsFound(self, ss: List[str]) -> int:
            return max(s.count(" ") for s in ss) + 1