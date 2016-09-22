
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