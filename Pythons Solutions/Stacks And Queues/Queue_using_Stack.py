"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
"""
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]
        self.flag=0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        
        self.stack1.append(x)
           
        

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.stack1)!=0 and self.flag==0:
            self.stack2.append(self.stack1.pop())#put everything in stack2
        self.flag=1#lock stack1 popping till stack2 is empty
        if len(self.stack2)!=0 and self.flag==1:
           return self.stack2.pop()
        else:
            self.flag=0
            
           
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack2)!=0:
            return self.stack2[-1]
        else:
            return self.stack1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack1) or len(self.stack2):
            return False
 else:
            return True