import  collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 深度优先
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:  # 两个节点都空就是相同的
        return True
    elif not p or not q:  # 两个节点只有一个空肯定不同
        return False
    elif p.val != q.val:  # 剩下一种可能是两个节点都存在，这时候判断节点值是否相等
        return False
    else:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 广度优先
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    # 广度优先都要把节点储存起来，一边分析一边检查有没有分析完
    queue1 = collections.deque([p])
    queue2 = collections.deque([q])

    # 当其中一个queue分析完，跳出循环
    while queue1 and queue2:
        node1 = queue1.popleft()
        node2 = queue2.popleft()

        if node1.val != node2.val:  # 实际上只需要对比传进来的节点，子节点递归函数进行对比
            return False

        left1, right1 = node1.left, node1.right
        left2, right2 = node2.left, node2.right

        # 以下主要分析存在性，如果一个有另一个没有就肯定不相同，直接可以出答案
        if (not left1) ^ (not left2):
            return False
        if (not right1) ^ (not right2):
            return False
        if left1:
            queue1.append(left1)
        if right1:
            queue1.append(right1)
        if left2:
            queue2.append(left2)
        if right2:
            queue2.append(right2)

    # 当分析完，如果是相同的话，那么两个queue都应该为None，所以return为True
    return not queue1 and not queue2
