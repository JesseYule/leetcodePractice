import heapq
import collections


def topKFrequent(words, k):
    count = collections.Counter(words)  # 直接统计每个单词出现次数，输出为字典
    heap = [(-freq, word) for word, freq in count.items()]  # 注意把频率变为负号，非常关键
    print(heap)

    heapq.heapify(heap)
    print(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]  # pop出k个结果的意思


# 自己的思路，主要问题是太慢
def customTopKFrequent(words, k):

    count = collections.Counter(words)  # 直接统计每个单词出现次数，输出为字典

    count1 = list(count)
    count2 = list(count.values())

    for i in range(len(count2)):
        count2[i] = count2[i] * -1

    merge = []

    for i in range(len(count1)):
        merge.append([count2[i], count1[i]])

    merge.sort()

    output = []

    for i in range(k):
        output.append(merge[i][1])

    return output


words = ["i", "love", "leetcode", "i", "love", "coding"]
print(customTopKFrequent(words, 2))