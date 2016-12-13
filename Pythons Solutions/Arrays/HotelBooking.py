"""
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .
"""

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    
    def hotel(self, arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)
       

        guests = 0

        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1

            if guests > K:
                return 0

        return 1

"""
READ CLASS IN PYTHON
Also List can be concatenated since it is mutable

NOTE SORTED IS BETTER TO USE IN CASE YOU HAVE COMPLEX ITEM IS LIST 
LAMBDA FUNC CAN BE USED TO SORT ON BASUS OF SOME ATTRIBUTE
READ IT DEEPER AT

https://docs.python.org/2/howto/sorting.html
"""

