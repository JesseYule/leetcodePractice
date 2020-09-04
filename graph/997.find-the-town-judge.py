# 自己写的，严重超时
def findJudge(N, trust):

    trust_num = [0] * N

    for i in range(len(trust)):
        trust_num[trust[i][1]-1] += 1

    if N-1 in trust_num:
        target = trust_num.index(N-1)
    else:
        return -1

    for i in range(len(trust)):
        if [target+1, i+1] in trust:
            return -1

    if target is None:
        return -1

    return target + 1


# 别人写的，速度快很多
# 遍历 trust，如果 trust[i] 为 [a, b] 说明 a 信任 b，那么更新 a 的出度 + 1，b 的入读 + 1。
# 遍历所有节点，将满足出度为0，入度为 N - 1的节点输出。

def findJudge(N, trust):
    in_degree = [0] * (N + 1)
    out_degree = [0] * (N + 1)
    for a, b in trust:
        in_degree[b] += 1
        out_degree[a] += 1
    for i in range(1, N + 1):
        if in_degree[i] == N - 1 and out_degree[i] == 0:
            return i
    return -1
