class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        r=len(A)
        c=len(A[0])
        count=0
        visited=[[False for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if A[i][j]=='X' and not visited[i][j]:
                    self.dfs(A,i,j,r,c,visited)
                    count+=1
        return count            
                    
    def dfs(self,A,i,j,r,c,visited):
            if i<0 or i>=r:
                return
            if j<0 or j>=c:
                return
            if A[i][j]=='O' or visited[i][j]:
                return
            visited[i][j]=True
            self.dfs(A,i+1,j,r,c,visited)
            self.dfs(A,i-1,j,r,c,visited)
            self.dfs(A,i,j+1,r,c,visited)
            self.dfs(A,i,j-1,r,c,visited)
        
        

        