# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    # 前面判断空与非空的情况，只有两个都非空才需要递归分析
    p1 = root
    q1 = root

    def analyse(p, q):
        if p is None and q is None:
            pass  # 子节点都为空只能说达到了数的最低端，要完整分析完整棵树
        elif p is None or q is None:  # 因为上面已经排除了两个都是None，所以这里只能是其中一个为None
            return False
        elif p.val != q.val:
            return False
        else:  # 如果来到这里，就证明两个节点的value存在且相等，所以继续分析子节点
            analyse(p.left, q.right)  # 对子节点而已，因为是镜像分析，所以左节点对应右节点
            analyse(p.right, q.left)

    analyse(p1, q1)

    return True



p1 = TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}
q1 = TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}