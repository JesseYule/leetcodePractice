class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 深度优先搜索
def depthMaxDepth(root):

    if not root:
        return 0

    curr_node = [root, 1]
    max = 1

    def findMax(curr_node, max):

        if curr_node[1] > max:
            max = curr_node[1]

        if curr_node[0].children:
            for i in range(len(curr_node[0].children)):
                max = findMax([curr_node[0].children[i], curr_node[1]+1], max)

        return max

    max_layer = findMax(curr_node, max)

    return max_layer


# 广度优先搜索
def breadthMaxDepth(root):

    # 处理边界情况
    if not root:
        return 0

    queue = [[root, 1]]  # 广度优先搜索都需要一个队列辅助

    def findMax(queue, max_layer):

        print(queue)

        curr = queue.pop(0)

        curr_node = curr[0]
        curr_layer = curr[1]

        if curr_layer > max_layer:
            max_layer = curr_layer

        if curr_node.children:
            for i in range(len(curr_node.children)):
                queue.append([curr_node.children[i], curr_layer+1])

            for i in range(len(curr_node.children)):  # 强行广度遍历
                max_layer = findMax(queue, max_layer)

        return max_layer

    result = findMax(queue, 1)

    return result


# ————————————————————————————————————————————————————官方答案————————————————————————————————————————————————————

# 递归

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1


# 迭代

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))

        return depth





