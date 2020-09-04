# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 所谓链表，实际上这里传入的分别是链表l1和l2的第一个元素，因为链表元素是有指向的，所以只要传入第一个元素就相当于传入了整个链表
    # 所以这里的合并链表的传入参数是两个listnode

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # prehead永远指向第一个节点
        prehead = ListNode(-1)

        tmp = prehead  # 这里就是为了复制一个其实的节点，为了下面的处理

        while l1 and l2:
            # 当l1和l2都不为空时
            if l1.val < l2.val:

                # 再次记住，l1和l2都是链表里面的一个元素，此时对比两个元素的大小，小的那个就是新的链表的起点，如果是第一次处理，就是prehead应该指向的元素
                tmp.next = l1
                l1 = l1.next  # 这两句话的作用相当于把第一个元素pop出来，从l1 pop到合并的链表中

            else:
                tmp.next = l2
                l2 = l2.next

            # 注意tmp = tmp.next和tmp.next = l1的区别
            tmp = tmp.next

        tmp.next = l1 if l1 is not None else l2

        # 这里的return就很讲究了，再次，因为链表的定义，我们返回时其实不是返回完整一个'链表'这样一个结构，或者说我们不能像数组、矩阵那样
        # 把链表写出来，这里选择的是把新的链表的第一个元素return回来
        return prehead.next
