# Definition for singly-linked list.
# Problem - 1721
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        kth_node = None
        head_iter = head
        k_temp = 1
        while(k_temp < k and head_iter is not None):
            head_iter = head_iter.next
            k_temp+=1
        
        k_start = head_iter;
        k_end = head;
        
        while(head_iter.next is not None):
            k_end = k_end.next
            head_iter = head_iter.next
        
        temp_val = k_start.val
        k_start.val = k_end.val
        k_end.val = temp_val
        return head
