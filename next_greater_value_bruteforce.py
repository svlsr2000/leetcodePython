# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_next_biggest(self,head:ListNode, number:int)->int:
        while(head is not None):
            if head.val > number:
                return head.val
            else:
                head = head.next
        return 0
    
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ret = []
        while(head is not None):
            next_big = self.find_next_biggest(head.next,head.val)
            ret.append(next_big)
            head = head.next
        return ret
