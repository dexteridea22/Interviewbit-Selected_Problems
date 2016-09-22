"""
Implement int sqrt(int x). Compute and return the square root of x.
If x is not a perfect square, return floor(sqrt(x))
"""
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low=1
        high=A
        found=False
        if A==0 or A==1:
           return A    
        while low<=high:
            mid=(low+high)/2
            if mid*mid==A:
               found=True 
               return mid
            elif mid*mid>A:
               high=mid-1
            else:
               low=mid+1
        if not found:
           return low-1    