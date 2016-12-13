import heapq
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    
    def mergeKLists(self, A):
        #print A[0].next.val
        dummy=Node=ListNode(0)
        heap=[(n.val,n) for n in A if n]
        heapq.heapify(heap)
        while heap:
            v, n = heap[0]
            if n.next is None:
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap,(n.next.val,n.next))
            Node.next=n
            Node=Node.next
            Node.val=v
        return dummy.next
