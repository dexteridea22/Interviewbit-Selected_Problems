"""
For Given Number N find if its COLORFUL number or not
Return 0/1
"""
class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        str(A)
        hashset=set([])
        l=[int(i) for i in list(str(A))]
        for i in range(0,len(l)-1):
            product=l[i]
            if product not in hashset:
                hashset.add(product)
            else:
                return 0
                break
            j=i+1
            while j<len(l):
               product*=l[j]
               if product not in hashset:
                   hashset.add(product)
               else:
                   return 0
                   break
               j+=1
               
            
        if l[len(l)-1] not in hashset:
            return 1
        else:
            return 0