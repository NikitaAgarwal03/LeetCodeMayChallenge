# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p1 = head
        headOfEvens = head.next
        p2 = head.next
        while p2:
            p1.next = p2.next
            if p1.next:
                p2.next = p1.next.next
            if p1 and p1.next:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        p1.next = headOfEvens
        
        return head
                
                
                
            
        
