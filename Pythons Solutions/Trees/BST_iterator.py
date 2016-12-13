"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.
"""

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        temp=root
        while temp!=None:
            self.stack.append(temp)
            temp=temp.left               #put in stack the first smallest elements inleft subtree

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack)!=0:
            return True
        else:
            return False
        

    def next(self):
        """
        :rtype: int
        """
        if len(self.stack)!=0:
           
            curr=self.stack.pop()
            nextsmall=curr
            if curr.right!=None:
               curr=curr.right
               while curr!=None:
                     self.stack.append(curr) #In case rightchild exists repeat the same on left subtree of right child
                     curr=curr.left
            return nextsmall.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())