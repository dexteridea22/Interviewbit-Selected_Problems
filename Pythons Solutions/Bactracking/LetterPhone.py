class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        if not A:
            return []
        dic={'0':'0','1':'1','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(A)==1:
            return list(dic[A])
        res=[]    
        self.dfs(A,dic,0,'',res)
        return res
    def dfs(self,A,dic,index,path,res):
        if len(A)==len(path):
            res.append(path)
            return
        for i in xrange(index,len(A)):
            for j in dic[A[i]]:
                self.dfs(A,dic,i+1,path+j,res)
                