 
class Solution(object):
    def removeNthFromEnd(self, head, n):
        left = right = head
        for i in range(n):
            right = right.next
            
        if not right:
            return left.next
        
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head