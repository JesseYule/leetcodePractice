class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head, val):

    prehead = ListNode(-1)
    output = prehead

    while head:

        if head.val != val:
            prehead.next = head
            prehead = prehead.next
        else:
            prehead.next = None
            # 这步很关键，假设链表后面的元素都是要删除的元素，比如1-2-3-3-3，要删除3，
            # 那么之前prehead指向了2就停了，直到结束都没有变化，可是2是默认指向3-3-3的，所以一定要把默认的指针改掉

        head = head.next

    return output.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(3)


a.next = b
b.next = c
c.next = d
d.next = e

print(removeElements(a, 3).val)
print(removeElements(a, 3).next.val)
print(removeElements(a, 3).next.next.val)
print(removeElements(a, 3).next.next.next.val)
print(removeElements(a, 3).next.next.next.next.val)