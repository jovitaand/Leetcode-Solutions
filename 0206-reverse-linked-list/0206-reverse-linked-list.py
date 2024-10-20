class Solution(object):
    def reverseList(self, head):
        if head == None:
            return
        next = None
        current = head
        prev = None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            head = prev
        return prev