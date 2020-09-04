class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):

    prehead = ListNode(-1)
    result = prehead

    while head:
        if head.next is None:
            prehead.next = head
            break
        elif head.next.val == head.val:
            head = head.next
            continue
        elif head.next.val != head.val and head.next is not None:
            prehead.next = head
            prehead = prehead.next
            head = head.next
        else:
            head = head.next

    return result.next


a = ListNode(1)
b = ListNode(1)
c = ListNode(3)
d = ListNode(4)
e = ListNode(4)


a.next = b
b.next = c
c.next = d
d.next = e


print(deleteDuplicates(a).val)
print(deleteDuplicates(a).next.val)
print(deleteDuplicates(a).next.next.val)
print(deleteDuplicates(a).next.next.next)


