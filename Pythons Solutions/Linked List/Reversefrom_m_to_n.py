"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL._
"""

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, head, m, n):
        if m==n or head is None:
            return head
        dummyNode=ListNode(0)
        dummyNode.next=head
        prev=dummyNode
        for i in range(m-1):
            prev=prev.next
        current=prev.next    
        reverse=None
        for i in range(n-m+1):
            Next=current.next
            current.next=reverse
            reverse=current
            current=Next
        prev.next.next=current
        prev.next=reverse
        
        return dummyNode.next
