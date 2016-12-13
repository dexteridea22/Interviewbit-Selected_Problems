"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:#IF THE TREE HAS ONLY ONE NODE
            return 0
        return self.sumup(root)
    def sumup(self,root):    
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        sum_left=self.sumup(root.left)
        if root.right!=None and root.right.left is None and root.right.right is None:#JUST AS YOU CALCULATE SUM OF LEAF NODE JUST CHECK IF IT IS A RIGHT LEAF NODE SIMPLY SET SUM_RIGHT RO ZERO ELSE GO IN SIMILAR FASHION
            sum_right=0
        else:    
           sum_right=self.sumup(root.right)# GO IN SIMILAR FASHION
        #print sum_left+sum_right
        return sum_left+sum_right# RETURN THE CALCULATED VALUE FROM LEFT SUBTREE AND RIGHT SUBTREE
        