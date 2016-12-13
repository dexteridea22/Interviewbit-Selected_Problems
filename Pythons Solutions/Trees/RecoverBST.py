class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, root):
        prev=None
        pred=None
        first=None
        second=None
        curr=root
        res=[]
        while curr!=None:
            if prev!=None and prev.val>curr.val:
                if first is None:
                    first=prev
                second=curr
                
            if curr.left is None:
                prev=curr
                curr=curr.right
            else:
                pred=curr.left
                while pred.right!=None and pred.right!=curr:
                    pred=pred.right
                if pred.right is None:
                    pred.right=curr
                    curr=curr.left
                else:
                    pred.right=None
                    prev=curr
                    curr=curr.right
        if first!=None and second!=None:
           if first.val<second.val:    
             res.append(first.val)
             res.append(second.val)
           else:
     
             res.append(second.val)
             res.append(first.val)
        return res       
