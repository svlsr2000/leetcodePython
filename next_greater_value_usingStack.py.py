# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ret = []
        stack_val = []
        index = 0
        while head is not None:
            ret.append(0)
           
            
            while stack_val:
                (top_index,top) = stack_val[-1]
                if top < head.val:
                    ret[top_index] = head.val
                    stack_val.pop()
                else:
                    break

            stack_val.append((index,head.val))
            index = index + 1
            head = head.next
        return ret
    
        
