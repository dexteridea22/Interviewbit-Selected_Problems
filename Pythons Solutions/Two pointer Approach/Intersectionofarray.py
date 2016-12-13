"""
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        length_A=len(A)
        length_B=len(B)
        i=0
        j=0
        res=[]
        while i<length_A and j<length_B:
            if A[i]==B[j]:
                res.append(A[i])
                i+=1
                j+=1
            elif A[i]>B[j]:
                j+=1
            elif A[i]<B[j]:
                i+=1
        if len(res)>0:
            return res
        else:
            return []