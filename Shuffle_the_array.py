from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #seperate length of array half
        # - if length is 6 than half lenght would be 3
        # separate array with two: length of 3 and other 3
        # there would be two arrays
        # and than second array should be inserted into first array with zigzag position
        # x1 y1 like this
        # intertwine two lists

        #my solution
        #ew_array = []
        #for i in range(n):
        #   new_array.append(nums[i])
        #   new_array.append(nums[i+n])
        #return new_array

        '''
            In this code, the first list comprehension [nums[i] for i in range(n) for _ in range(2)] generates a list containing the first n elements of nums, repeated twice. It does this by iterating over the indices in the range from 0 to n-1, and using each index to retrieve the corresponding element from nums, then repeating each element twice using the for _ in range(2) syntax.

            The second line assigns the values of the second n elements of nums to every other element in the new_array, starting from index 1, using the slice notation [1::2].

            The result of this code is the same as the original code that appends the elements of nums to new_array using a for loop.
        '''

        new_array = []

        new_array = [nums[i] for i in range(n) for e in range(2)]
        new_array[1::2] = [nums[i+n] for i in range(n)]
        return new_array

        #other solution
        # simple and readable and also runtime was shortest
        # x = nums[:n]
        # y = nums[n:]
        # is this part should be added?
        # # x.sort()
        # # y.sort()
        #
        # res = []
        #
        # for i in range(n):
        #     res.append(x[i])
        #     res.append(y[i])
        #
        # return res

        #love this solution
        #easy to understand and code is readable

        # nums = [2,5,1,3,4,7]
        # n = 3
        # the nums array is currently structured as [x1,x2,x3,y1,y2,y3]
        # must return in this order [x1,y1,x2,y2,x3,y3]
        # n represents the amout of indexes we must jump over to retrieve the element we are looking for
        # Step 1 - create an empty array
        # Step 2 - grab the first element and add it to the new array
        # Step 3 - loop over the array n times and append that value to the array
        # Step 4 - return new array



        # result = [0] * (2 * n) # this creates a list of 0's of 2 x 3 which is [0,0,0,0,0,0]
        #
        # for i in range(n):
        #     result[2 * i] = nums[i]
        #     result[2 * i + 1] = nums[n + i]
        # return result