"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        prevmax=float('-inf')
        prevmin=float('inf')
        maxprofit=0
        for i in range(0,len(A)):
            if A[i]<prevmin:#if A[i] less than previously found minimum we will update both max and min tiil now to A[i]
                prevmin=A[i]
                prevmax=A[i]
            elif prevmax<A[i]:# if A[i] is greater than prevmax we will update prevmax
                prevmax=A[i]
            maxprofit=max(maxprofit,prevmax-prevmin)   
        return maxprofit    
