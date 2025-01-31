# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            #If list1.val is smaller, attach it to the recursive result of list1.next and list2.
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            #If list2.val is smaller, attach it to the recursive result of list1 and list2.next.
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2