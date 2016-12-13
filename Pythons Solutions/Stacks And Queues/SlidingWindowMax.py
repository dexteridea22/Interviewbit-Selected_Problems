"""
A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position.

Example :

The array is [1 3 -1 -3 5 3 6 7], and w is 3.

Window position	Max
 	 
[1 3 -1] -3 5 3 6 7	3
1 [3 -1 -3] 5 3 6 7	3
1 3 [-1 -3 5] 3 6 7	5
1 3 -1 [-3 5 3] 6 7	5
1 3 -1 -3 [5 3 6] 7	6
1 3 -1 -3 5 [3 6 7]	7
Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]

 Note: If w > length of the array, return 1 element with the max of the array. 
"""
from collections import deque
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        res=[]
        d=deque()
        for i,n in enumerate(A):
            while d and A[d[-1]]<n: #Keep popping out if no. s less than current element because they are of no use
                d.pop()
            d.append(i)
            if d[0]==i-B:       #First element in queue is of no use now
                d.popleft()
            if i>=B-1:          # You have now processed winow of size k ouput answer at head of queue  
                res.append(A[d[0]])
        return res
                        
                    
        
