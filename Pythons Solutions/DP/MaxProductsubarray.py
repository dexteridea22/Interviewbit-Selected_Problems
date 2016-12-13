"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
Return an integer corresponding to the maximum product possible.
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A)==0:
            return 0
        maxprod=A[0]
        minprod=A[0]
        maxprodres=A[0]
        for i in range(1,len(A)):
            if A[i]<0:
                maxprod,minprod=minprod,maxprod
            maxprod=max(maxprod*A[i],A[i])#either prev max*A[i] is maximum or current A[i] is maximum
            minprod=min(minprod*A[i],A[i])#why we need this bcse -ve no.may appear  either prev min*A[i] is minimum or current A[i] is minimum
            maxprodres=max(maxprod,maxprodres)#to keep track of prev found max product subarray
        return maxprodres    