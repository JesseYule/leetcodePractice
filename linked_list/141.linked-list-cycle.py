# 这题的解法厉害到飞起，快慢指针，应该是一种技巧
# 判断是不是环形链表，看成一个环形操场，两个人跑步，一块一慢，如果是环形的话最后两人肯定会相遇，
# 否则会有人跑到终点然后break


def hasCycle(head):

    # 如果传入的是空链表或者链表的下一个指向None，则直接输出False，不存在环形结构
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:  # 当其中一个是None，就证明可以到达终点，也就是链表不是环形的
            return False
        slow = slow.next
        fast = fast.next.next  # 主要是这里的两个next反映出速度的差距，刚好快了一步
    return True
