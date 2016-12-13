"""
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=sorted(nums)
        if len(num)==1:
            return num[0]
        i=0;
        while i<len(num):
            
            if num[i+2]^num[i]!=0 or num[i]^num[i+1]!=0:
               return num[i]
               break
            else:
               i+=3
               if i==len(num)-1:
                  return num[i]