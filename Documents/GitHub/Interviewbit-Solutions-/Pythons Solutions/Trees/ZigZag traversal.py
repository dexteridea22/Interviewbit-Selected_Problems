"""
Given a binary tree, return the zigzag level order traversal of its nodes’ values. 
(ie, from left to right, then right to left for the next level and alternate between)
"""
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, root):
        finalres=[]
        res=[]
        if root is None:
            return []
        s1=[]
        s2=[]
        s1.append(root)
        flag=0
        while len(s1)>0 or len(s2)>0:
            if len(s1)>0:
                res=[]
            while len(s1)>0:
                root=s1.pop()
                res.append(root.val)
                if root.left is not None:
                    s2.append(root.left)
                if root.right is not None:
                    s2.append(root.right)
            finalres.append(res)
            if len(s2)>0:
                res=[]

            while len(s2)>0:
                root=s2.pop()
                res.append(root.val)
                flag=1
                if root.right is not None:
                    s1.append(root.right)
                if root.left is not None:
                    s1.append(root.left)
            if flag==1:
                flag=0
                finalres.append(res)        
        return finalres
    
