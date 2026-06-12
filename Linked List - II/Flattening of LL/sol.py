class Solution:

    def merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.val <= b.val:
            result = a
            result.child = self.merge(a.child, b)
        else:
            result = b
            result.child = self.merge(a, b.child)

        result.next = None
        return result

    def flattenLinkedList(self, head):
        if head is None or head.next is None:
            return head

        head.next = self.flattenLinkedList(head.next)

        return self.merge(head, head.next)