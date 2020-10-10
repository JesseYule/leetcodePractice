class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1_num = 0
    mul = 1

    while True:
        l1_num += l1.val * mul
        mul *= 10
        if l1.next:
            l1 = l1.next
            print(l1)
        else:
            break

    print(l1_num)
    l2_num = 0
    mul = 1

    while True:
        l2_num += l2.val * mul
        mul *= 10
        if l2.next:
            l2 = l2.next
        else:
            break

    print(l2_num)
    result = l1_num + l2_num

    result = str(result)
    result = result[::-1]

    output_node = ListNode(int(result[0]))
    output = output_node
    for i in range(len(result)-1):
        output_node.next = ListNode(int(result[i+1]))
        output_node = output_node.next

    return output


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

addTwoNumbers(node1, node1)