"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null. 
Try solving it using constant additional space.
"""
class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, head):
     
        if head is None:
            return None
        slow=head
        fast=head.next
        while slow!=fast and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        size=0    
        if slow==fast:
            temp=fast.next
            while temp!=fast:
                size+=1
                temp=temp.next
            size+=1
            newtemp=head
            while size>0:
                newtemp=newtemp.next
                size-=1
            while head!=newtemp:
                head=head.next
                newtemp=newtemp.next
            return head
        else:
            return None
                