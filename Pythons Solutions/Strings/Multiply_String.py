"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #l1=[int(i) for i in num1]
        #l2=[int(i) for i in num2]
        val=0
        carry=0
        sum=0
        flag=0
        product=0
        res=[]
        k=0
        i=len(num1)-1
        j=len(num2)-1
        flag=0
        if len(num1)>len(num2):
           i,j=j,i
           flag=1

        while i>=0:
                res=[]
                while j>=0:
                    if flag==1:
                       val=((int(num2[i])*int(num1[j]))+carry)
                    else:   
                       val= ((int(num1[i])*int(num2[j]))+carry)  
                    res=[str(val%10)]+res
                    #print res
                    carry=val/10
                    j-=1
                if carry!=0:    
                    res=[str(carry)]+res    
                product=int(''.join(res)) 
                carry=0
               # print product
                sum=sum+((product)*(10**k))
                #print sum
                k+=1
                i-=1
                if flag==1:
                   j=len(num1)-1
                else:   
                   j=len(num2)-1 
        return str(sum)   
        
                