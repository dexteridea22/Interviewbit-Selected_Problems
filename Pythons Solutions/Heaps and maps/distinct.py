rom collections import deque
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
   
    def dNums(self, A, B):
        j=0
        res=[]
        if B>len(A):
            return res
        hashmap={}
        for i in xrange(len(A)):
            hashmap[A[i]]=0
        #print hashmap
        k=0
        i=0
        k=0
        distcount=0
        while j<len(A):
            while j<len(A) and k!=B: 
               hashmap[A[j]]+=1
               if hashmap[A[j]]==1:
                  distcount+=1
               j+=1
               k+=1
            prevcount=distcount   
            res.append(distcount)
            hashmap[A[i]]-=1
            k-=1
            if hashmap[A[i]]!=0:
                distcount=prevcount
            else:
                prevcount-=1
                distcount=prevcount
            i+=1    
        return res    
            
                