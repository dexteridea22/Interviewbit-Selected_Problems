class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, s):
        res=[]
        self.dfs(s,[],res)
        return res
        
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
            return
        
        for i in range(1,len(s)+1):
           
            if self.ispalin(s[:i]):
                self.dfs(s[i:],path+[s[:i]],res)
                
    def ispalin(self,s):
        if s==s[::-1]:
            return 1
        else:
            return 0
