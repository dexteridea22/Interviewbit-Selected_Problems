#Given n non-negative integers a1, a2, ..., an,where each represents a point at coordinate (i, ai).'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
#Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#Your program should return an integer which corresponds to the maximum area of water that can be contained ( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        if len(A)==1:
            return 0
            
        i=0
        j=len(A)-1
        
        maxarea=0
        while i<j:
            maxdist=j-i
            maxarea=max(maxarea,(min(A[i],A[j])*maxdist))
            if A[i]<A[j]:
                i+=1
            else:
                j-=1
        return  maxarea      
