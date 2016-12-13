import heapq
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        count=0
        for i in range(0,len(B)):
            B[i]=-B[i]
         
        heapq.heapify(B)   
       # print B  
        while A:
           
           if B[0]==0:
               break
           count+=abs(heapq.heapreplace(B,-int(math.floor(-B[0]/2))))
          # print B
           A-=1
        return (count)%1000000007 