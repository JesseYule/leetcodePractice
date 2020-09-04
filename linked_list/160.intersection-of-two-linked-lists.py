#  又是一个无敌的方法，创建两个指针 pApA 和 pBpB，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
#  当 pApA 到达链表的尾部时，将它重定位到链表 B 的头结点 (你没看错，就是链表 B); 类似的，当 pBpB 到达链表的尾部时，
#  将它重定位到链表 A 的头结点。若在某一时刻 pApA 和 pBpB 相遇，则 pApA/pBpB 为相交结点。

#  A和B两个链表长度可能不同，但是A+B和B+A的长度是相同的，
#  所以遍历A+B和遍历B+A一定是同时结束。 如果A,B相交的话A和B有一段尾巴是相同的，
#  所以两个遍历的指针一定会同时到达交点 如果A,B不相交的话两个指针就会同时到达A+B（B+A）的尾节点


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):

    if not headA or not headB:
        return None

    nodeA = headA
    nodeB = headB

    while (nodeA != nodeB):
        # 无敌，一直遍历到nodeA的尽头，此时为None，且无下一个指向的元素，
        # 此时马上把nodeA接到headB，继续遍历
        # 注意，这里很关键，nodeA会变成None，也就是整个链表此时认为是1>2>3>...>None
        # None也是链表的一部分，所以假如两个链表没有重合，实际上遍历到最后也会在None重合
        # 假设两个链表有重合，那么在到达None之前就会重合然后退出
        nodeA = nodeA.next if nodeA else headB
        nodeB = nodeB.next if nodeB else headA

    return nodeA


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)


a.next = b

c.next = d
d.next = e

print(getIntersectionNode(a, c))