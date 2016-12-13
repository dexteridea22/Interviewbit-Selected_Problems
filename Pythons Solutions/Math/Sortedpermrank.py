"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
Assume that no characters are repeated.

Example :
Input : 'acb'
Output : 2
The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
"""

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        i=0
        length=len(A)
        rank=1
        while i<len(A)-1:
            first=A[i]
            small=0
            j=i+1
            while j<len(A):
                if first>A[j]:
                    small+=1
                j+=1    
            rank+=small*math.factorial(length-1)
            length-=1
            i+=1
        return rank%1000003    
