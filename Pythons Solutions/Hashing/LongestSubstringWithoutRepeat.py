"""
Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
"""
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        hashmap={}
        i=0
        j=0
        maxlen=1
        while j<len(A):
           if A[j] not in hashmap:
               hashmap[A[j]]=j
               j+=1
           else:
               maxlen=max(maxlen,j-i)#Maintain a sliding Window with i,j as its start and end
               #print maxlen
               i=hashmap[A[j]]+1#Reset i and j ie the size of sliding window is now zero and start from fresh
               j=i
               del hashmap
               hashmap={}
        #print i,
        #print j
        maxlen=max(maxlen,j-i)#if j goes till last else part will not execute so tackle it I code this statement
        #print maxlen
          
        return maxlen   