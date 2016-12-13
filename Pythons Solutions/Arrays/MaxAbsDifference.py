"""
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        arr_diff=[]
        arr_sum=[]
        for i in range(0,len(A)):
            arr_diff.append((A[i]-i))
            arr_sum.append((A[i]+i))
        #print arr_diff
        #print arr_sum
        min_diff=min(arr_diff)
        #print min_diff
        max_diff=max(arr_diff)
        #print max_diff
        min_sum=min(arr_sum)
        #print min_sum
        max_sum=max(arr_sum)
        #print max_sum
        return max((max_sum-min_sum,max_diff-min_diff))
