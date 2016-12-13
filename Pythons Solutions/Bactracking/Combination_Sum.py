class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, T):
        res=[]
        hashmap={}
        path=[]
        sum_=0
        A.sort()
        track=''
        self.backtracksum(A,path,res,sum_,T,0,track,hashmap)
        return res
    def backtracksum(self,A,path,res,sum_,T,index,track,hashmap):
        if sum_>T:
            return
        if sum_==T and track not in hashmap:
            res.append(path)
            hashmap[track]=1
            return
        for i in range(index,len(A)):
            self.backtracksum(A,path+[A[i]],res,sum_+A[i],T,index,track+str(A[i]),hashmap)
            index+=1
