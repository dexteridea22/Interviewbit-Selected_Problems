class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        res=[]
        self.findpermute(A,[],res)
        return res
        
    def findpermute(self,A,path,res):
        if len(A)==0:
            res.append(path)
            return 
        
        for i in range(0,len(A)):
            self.findpermute(A[:i]+A[i+1:],path+[A[i]],res)
