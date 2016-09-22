"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand. 
(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).You are given a target value to search. If found in the array, return its index, otherwise return -1.
You may assume no duplicate exists in the array.
"""
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, nums, target):
        midIndex=self.findminIndex(nums)
        if nums[midIndex]==target:
            return midIndex
        start=0
        end=len(nums)-1
        
        Lindex=self.Binarysearch(nums,start,midIndex-1,target)
        if Lindex!=-1:
            return Lindex
        else:    
           Rindex=self.Binarysearch(nums,midIndex+1,end,target)
           if Rindex!=-1:
              return Rindex
           else:
              return -1 
        
    def findminIndex(self,A):   
           low=0
           high=len(A)-1
           N=len(A)
           while low<=high:
              if A[low]<=A[high]:
                  return low
              mid=(low+high)/2
              next=(mid+1)%N
              prev=(mid+N-1)%N
              if A[mid]<=A[next] and A[mid]<=A[prev]:
                  return mid
              elif A[low]<=A[mid]:
                  low=mid+1
              else:
                  high=mid-1
    def Binarysearch(self,A,low,high,target):
           found=False
           while low<=high:
 mid=(low+high)/2
              if A[mid]==target:
                  found=True
                  return mid
              elif A[mid]<target:
                  low=mid+1
              else:
                  high=mid-1
           if not found:          
              return -1          
