class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val #to understand view the diagram
        node.next = node.next.next
        return