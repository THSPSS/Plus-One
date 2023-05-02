'''
Explanation
Alternatively append the character from w1 and w2 to res.


Complexity
Time O(n + m)
Space O(n + m)
'''
import itertools

class Solution:
    #not using zip
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word=""
        try :
            for i , w in enumerate(word1):
                new_word += w
                new_word += word2[i]
        except IndexError:
                new_word += word2[i:]
        new_word += word2[len(word1):]
        new_word += word1[len(word2)+1:]
        return (new_word)

    #using zip with for loop
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word =""
        for w1, w2 in zip(word1,word2):
            new_word += w1
            new_word += w2

        if len(word1) == len(word2):
            return new_word
        elif len(word1) > len(word2):
            rest = word1[len(word2):]
            new_word += rest
        else:
            rest = word2[len(word1):]
            new_word += rest
        return (new_word)

    #using max to choose maximum word and loop through and add each word
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        max_num = max(len(word1), len(word2))
        for num in range(max_num):
            if num < len(word1):
                new_word += word1[num]
            if num < len(word2):
                new_word += word2[num]

        return (new_word)



    #using itertools module that provides various functions that work on iterators to produce complex iterators
    def mergeAlternately(self, w1, w2):
        return ''.join(a + b for a, b in itertools.zip_longest(w1, w2, fillvalue=''))