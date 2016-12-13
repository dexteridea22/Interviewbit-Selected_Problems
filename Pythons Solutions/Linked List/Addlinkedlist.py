"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        q1=l1
        q2=l2
        dummy=ListNode(0)
        curr=dummy
        carry=0
        while q1!=None or q2!=None:
            if q1==None:
                x=0
            else:
                x=q1.val
            if q2==None:
                y=0
            else:
                y=q2.val
            sum=(x+y+carry)%10
            carry=(x+y+carry)/10
            curr.next=ListNode(sum)
            if q1!=None:
                q1=q1.next
  if q2!=None:
                q2=q2.next
            curr=curr.next
            
        if carry>0:
            curr.next=ListNode(1)
        return dummy.next    
                
            
         