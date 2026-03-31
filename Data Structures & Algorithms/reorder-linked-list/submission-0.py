# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #lets start by finding the first and second halfs
        slow = head
        fast = head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        second = slow.next 
        prev = None
        slow.next = None 

        #lets reverse the linked list in the second half 
        while second:
            tmp1 = second.next
            second.next = prev
            prev = second
            second = tmp1

        #lets assemble the linked list back 
        first = head 
        second = prev

        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1 
            first = tmp1
            second = tmp2


        




        


        