"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
"""

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1=[]
        self.q2=[]
        self.flag=0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.flag==0:
           self.q1.append(x)
        else:
           self.q2.append(x)    
            
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.flag==0:
          while len(self.q1)!=1:
             self.q2.append(self.q1.pop(0))
          self.flag=1      
          return self.q1.pop(0)  
        else:
            while len(self.q2)!=1:
             self.q1.append(self.q2.pop(0))
 self.flag=0      
            return self.q2.pop(0)  
            
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.q1)!=0:
            return self.q1[len(self.q1)-1]
        else:
            return self.q2[len(self.q1)-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.q1) or len(self.q2):
            return False
        else:
            return True
        