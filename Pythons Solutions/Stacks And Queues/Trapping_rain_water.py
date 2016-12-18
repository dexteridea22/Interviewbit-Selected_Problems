'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example :

Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, arr):
        trapped=0
        n=len(arr)
        j=n-1
        left_stack=[]
        right_stack=[]
        while j >= 0:
            if not right_stack:
                right_stack.append(arr[j])
            else:
                if right_stack:
                  if right_stack[-1] <= arr[j]:
                     right_stack.append(arr[j])
            j-=1
        #print right_stack
        i=0
        while i < n:
            if not left_stack:
                left_stack.append(arr[i])
                
            if right_stack and left_stack:    
                
                if left_stack[-1] > arr[i] and right_stack[-1] > arr[i]:
                    trapped+=min(left_stack[-1],right_stack[-1])-arr[i]
                elif arr[i] == right_stack[-1] and left_stack[-1]<right_stack[-1]:
                    left_stack.append(right_stack.pop())
                elif arr[i]==right_stack[-1]:
                    right_stack.pop()
                elif arr[i] > left_stack[-1]:
                    left_stack.pop()
                    left_stack.append(arr[i])
            i+=1    
                    
        return trapped
                    