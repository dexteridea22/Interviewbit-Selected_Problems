"""
Given a binary tree, flatten it to a linked list in-place.

Example :
Given
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.
"""
class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        stack=[]
        root=A
        while len(stack)!=0 or A!=None:
            if A.right!=None:
                stack.append(A.right)
            if A.left!=None:
                A.right=A.left
                A.left=None
            elif len(stack)!=0:
                temp=stack.pop()
                A.right=temp
            
            A=A.right  
        return root    
