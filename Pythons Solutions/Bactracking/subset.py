class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        res=[]
        path=[]
        if len(A)==0:
            return [[]]
        A.sort()    
        return self.sub_set(A,path,res,0)
        
    def sub_set(self,A,path,res,index):
        res.append(path)
       # if index>=len(A):
            #return 
        
        for i in range(index,len(A)):
            self.sub_set(A,path+[A[i]],res,i+1)
        return res    
