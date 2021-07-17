#23. Merge k Sorted Lists problem url - https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = []
        i = 0

# Initialize a sequence of lists 
# [ h0 [1,4,5],
#  h1 [1,3,4],
#  h2 [2,6]]

        for head in lists:
            if head is not None:
                heads.append( head )
                i = i + 1
    #initialize the list to be populated and also what has to be returned       
        retList = None
        retNode = None
        
    # Process all the list
        while heads:
    # First assume first list is the minimum value
            mini = heads[0].val
            min_loc = 0
            j = 0
    # Now iterate through all the list and check which list is having minimum
           # print("i = {}".format(i))
            while j < i:
                #print("i = {} , j = {} ".format(i,j))
                if mini > heads[j].val:
    #Minimum is found now take note of minimum and location of minimum
                    mini = heads[j].val
                    min_loc = j
                j = j +1
    # Insert into return list, if list is not found create none
            if retList is None:
                retList = ListNode(mini)
    # Take backup so that we can return the head
                retNode = retList
            else:
    # List already there let us insert into next item and move list ahead
                retList.next = ListNode(mini)
                retList = retList.next
    # Move the original list ahead
            heads[min_loc] = heads[min_loc].next

    #If the orginial list from where data is popped
            if heads[min_loc] is None:
                heads.pop(min_loc)
                i = i -1 

        return retNode
