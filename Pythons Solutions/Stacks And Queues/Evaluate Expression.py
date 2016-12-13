"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack=[]
        for i in range(0,len(A)):
            if A[i]!='+' and A[i]!='-' and A[i]!='/' and A[i]!='*':
                stack.append(A[i])
           
            else:
                if A[i]== '+':
                    first=stack.pop()
                    second=stack.pop()
                    stack.append(str(int(second)+int(first)))
                   
                elif A[i]== '-':
                    first=stack.pop()
                    second=stack.pop()
                    stack.append(str(int(second)-int(first)))
                    
                elif A[i]== '*':
                    first=stack.pop()
                    second=stack.pop()
                    stack.append(str(int(second)*int(first)))
                
                else:
                    
                    first=stack.pop()
                    second=stack.pop()
                    stack.append(str(int(second)/int(first)))
                  
        return int(stack.pop())            
                    
        
