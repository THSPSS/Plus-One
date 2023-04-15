class Solution:
    #mysolution
    #using for loop and append to list  and get max value from list
    def minPartitions(self, n: str) -> int:
        li = []

        for i in n:
            li.append(int(i))

        return max(li)

    #other solution
    #simplest solution
    #just pick max from n and convert data type and return it
    def ohterMinPartitions(self, x):
        return int(max(x))


    #clever solution
    #using list and from '9' to '0' placed in decending order
    #it basically loop through list and find first letter that true to if statement
    def minPartitions(self, n: str) -> int:
        for i in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']:
            if i in n:
                return int(i)




