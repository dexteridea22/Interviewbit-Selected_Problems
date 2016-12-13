"""
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
"""
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals)==0:
            return []
        intervals.sort(key=lambda i:i.start)# sort intervals on basis of start event
        curr=intervals[0]
        res=[]
        for i in intervals:
            if i.start<=curr.end:#Compare curr's end and i's start if true then overlap occur
                curr.end=max(i.end,curr.end)#Now update this Interval's end=max(i,end,curr.end)
            else:
                res.append(curr)
                curr=i
        res.append(curr)
        return res
