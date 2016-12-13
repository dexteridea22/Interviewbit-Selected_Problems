"""
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:		
Input: 	

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
"""
class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
	def diagonal(self, a):
	          R=len(a)
	          C=len(a[0])
	          finalres=[]
	          for D in xrange(2*(R-1)+1):# OBSERVE i+j=D
	              res=[]
	              for i in xrange(D+1):
	                  if i<R and D-i<C:
	                      res.append(a[i][D-i])
	              finalres.append(res)           
	          return finalres           

