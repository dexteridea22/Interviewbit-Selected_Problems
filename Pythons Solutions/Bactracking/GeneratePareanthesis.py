def generateParenthesis(self, A):
        open_=A
        close_=A
        ans=[]
        self.dfs(open_,close_,ans,'')
        return ans
    def dfs(self,open_,close_,ans,string):
        if open_>close_ or open_<0 or close_<0 :
            return
        if not open_ and not close_:
            ans.append(string)
        self.dfs(open_-1,close_,ans,string+'(')    
        self.dfs(open_,close_-1,ans,string+')')
        
