"""
Given a binary tree, invert the binary tree and return it. 
Look at the example for more details.

Example : 
Given binary tree

     1
   /   \
  2     3
 / \   / \
4   5 6   7
invert and return

     1
   /   \
  3     2
 / \   / \
7   6 5   4

"""
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is None:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)
           
        if(root.left is not None or root.right is not None):
            root.left,root.right=root.right,root.left
        return root  