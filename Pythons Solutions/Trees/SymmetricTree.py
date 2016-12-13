"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric. 
But the following is not:

    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return self.isMirror(A,A)
    def isMirror(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            if root1.val==root2.val:
               return self.isMirror(root1.left,root2.right) and self.isMirror(root1.right,root2.left)
        return False