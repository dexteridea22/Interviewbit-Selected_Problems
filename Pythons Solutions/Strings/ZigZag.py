"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
display this pattern in a fixed font for better legibility)
P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
"""

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
      i=0
      res=''
      rows=B
      if B==1   :
          return A
      n=len(A)
      if n==0:
          return ''
      if n<=B:
         return A 
      while i<B:
        j=i
        flag=0
        while j<len(A):
          res+=A[j]
          if rows!=1 and flag==0:
             j+=(2*rows-2)
             flag=1
          elif rows!=1 and flag==1 and rows!=B:
             j+=(2*B-2)-(2*rows-2)
             flag=0 
          else:
             j+=(2*B-2)
        rows-=1
        i+=1
      return res    