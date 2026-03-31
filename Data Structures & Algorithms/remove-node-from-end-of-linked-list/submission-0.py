# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Okay this ones not that hard 
        #we initialize two pointers, one at dummy and next one n steps ahead
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n>0 and right:
            right = right.next
            n -= 1

        #now we want to keep moving on step until right is at none
        while right:
            left = left.next
            right = right.next 

        #delete the node where our left pointer is 
        left.next =left.next.next
        return dummy.next

    

        



        


        
        