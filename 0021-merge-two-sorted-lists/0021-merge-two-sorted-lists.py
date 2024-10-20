class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val: #if list 1 is bigger than list 2
                tail.next = list1 #moving to the last node
                list1 = list1.next #updating the pointer
            else:
                tail.next = list2 #moving to the last node
                list2 = list2.next #updating the pointer
            tail = tail.next #updating the tail
            
        if list1: #if l1 is not null
            tail.next = list1 #print list 1
        elif list2: #print list 2 is null
            tail.next = list2 #print list 2
            
        return dummy.next #return the list
                
        