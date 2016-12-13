"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""



class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root==p or root==q:
           return root
           
        a=self.lowestCommonAncestor( root.left, p, q) 
        b=self.lowestCommonAncestor( root.right, p, q)
        if a is not None and b is not None:
           return root
        if a is not None and b is None:
           return a
        if a is None and b is not None:
           return b    