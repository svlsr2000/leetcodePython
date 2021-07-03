# This is solution for leet code problem number 1669
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def delete_nodes_from_list(list1:ListNode, a: int, b:int)->ListNode:
    head = list1
    first_item = head
    count = a - 1
    while count is not 0:
        first_item = first_item.next
        count = count - 1
    
    print("First item = {}".format(first_item.val))
    
    second_item = first_item
    count = b - (a -1)
    while count is not 0:
        second_item = second_item.next
        count = count - 1
    

    
    first_item.next = second_item.next
    
    return first_item
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start_pos = delete_nodes_from_list(list1,a,b)
        if start_pos is not None:
            end_pos = start_pos.next
        start_pos.next = list2
        
        while list2.next is not None:
            list2 = list2.next
        
        list2.next = end_pos
        
        return list1
