# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


# 深度优先搜索
class Solution(object):

    def __init__(self):
        self.visited = {}

    # 对于一张图而言，它的深拷贝即构建一张与原图结构，值均一样的图，但是其中的节点不再是原来图节点的引用

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:  # 如果传入一个空节点则直接return空节点，为了处理一开始就传入空节点的情况
            return node

        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]

        # 到了这里，就证明这个节点之前没被访问过，所以就克隆该节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])

        # 把新的节点储存在哈希表中，之后再访问就知道已经访问过了，避免死循环
        self.visited[node] = clone_node

        # 遍历该节点的邻居，同时根据实际情况进行递归、克隆
        if node.neighbors:
            # 这里会一层层递归到尽头，所以是深度优先搜索
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node


from collections import deque


# 广度优先搜索
class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        visited = {}

        # 将题目给定的节点添加到队列
        queue = deque([node])
        # 克隆第一个节点并存储到哈希表中
        visited[node] = Node(node.val, [])

        # 广度优先搜索
        while queue:
            # 取出队列的头节点
            n = queue.popleft()
            # 遍历该节点的邻居
            # 主要是这里遍历的方式改变了，这里是先把当前的邻居都遍历了，所以是广度优先
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # 如果没有被访问过，就克隆并存储在哈希表中
                    visited[neighbor] = Node(neighbor.val, [])
                    # 将邻居节点加入队列中
                    queue.append(neighbor)
                # 更新当前节点的邻居列表
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]
