class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 主要是找到两个节点的路径，然后对比得到结果
def lowestCommonAncestor(root, p, q):

    # 搜索树的性质导致搜索十分方便，不需要深度优先搜索或者广度优先搜索

    curr1 = root
    curr2 = root

    p_path = []
    q_path = []

    while curr1.val != p.val:
        if p.val > curr1.val:
            p_path.append(curr1)
            curr1 = curr1.right
        else:
            p_path.append(curr1)
            curr1 = curr1.left

    p_path.append(curr1)

    while curr2.val != q.val:
        if q.val > curr2.val:
            q_path.append(curr2)
            curr2 = curr2.right
        else:
            q_path.append(curr2)
            curr2 = curr2.left

    q_path.append(curr2)

    result = 0

    print(p_path)
    print(q_path)

    if p in q_path:
        print(p.val)
        return p

    if q in p_path:
        print(q.val)
        return q

    for i in range(len(p_path)):
        if p_path[i].val == q_path[i].val:
            result = p_path[i]
        else:
            break

    return result


node1 = TreeNode(6)
node2 = TreeNode(2)
node3 = TreeNode(8)
node4 = TreeNode(0)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(9)
node8 = TreeNode(3)
node9 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9


lowestCommonAncestor(node1, node2, node5)
