# def topKFrequent(nums, k):
#
#     freq = {}
#
#     for i in range(len(nums)):
#         if nums[i] not in freq:
#             freq[nums[i]] = 1
#         else:
#             freq[nums[i]] += 1
#
#     result = freq.items()
#     result = list(result)
#     for i in range(len(result)):
#         result[i] = list(result[i])
#
#     result = sorted(result, key=(lambda x: x[1]), reverse=True)
#
#     output = []
#
#     for i in range(k):
#         output.append(result[i][0])
#
#     return output
#
#
# nums = [4, 4, 1, 1, 1, 2, 2, 3]
# k = 2
# print(topKFrequent(nums, k))


# 这题我没有用堆做出来，但是像这种求top K、分位数的题目很适合用堆来做
# 最大堆适合做topk小问题，我们可以构建一个k个数的最大堆，根节点就是整个堆最大的，然后我们就遍历数据，用数据替换根节点
# 这样遍历一轮，这个最大堆剩下的数据就是整个数据集中最小的那k个数
# 之所以用最大堆做topk小问题，主要是因为我们可以确定替换的位置（根节点）

# 其实过程完全和我一样，只是最后排序的时候用了堆排序，我是直接用内置函数排序list


import collections


def topKFrequent(nums, k):

    def sift_down(arr, root, k):
        """下沉log(k),如果新的根节点>子节点就一直下沉"""
        val = arr[root] # 用类似插入排序的赋值交换
        while root<<1 < k:
            child = root << 1
            # 选取左右孩子中小的与父节点交换
            if child|1 < k and arr[child|1][1] < arr[child][1]:
                child |= 1
            # 如果子节点<新节点,交换,如果已经有序break
            if arr[child][1] < val[1]:
                arr[root] = arr[child]
                root = child
            else:
                break
        arr[root] = val

    def sift_up(arr, child):
        """上浮log(k),如果新加入的节点<父节点就一直上浮"""
        val = arr[child]
        while child>>1 > 0 and val[1] < arr[child>>1][1]:
            arr[child] = arr[child>>1]
            child >>= 1
        arr[child] = val

    stat = collections.Counter(nums)  # 相当于我用字典统计一次数量
    print('stat: ', stat)
    stat = list(stat.items())
    print('stat: ', stat)

    heap = [(0, 0)]

    # 一开始k个元素用来构建最小堆，后面的元素用来判断分析，所以既需要下沉也需要上浮

    # 构建规模为k+1的堆,新元素加入堆尾,上浮
    for i in range(k):
        heap.append(stat[i])
        sift_up(heap, len(heap)-1)

    # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
    for i in range(k, len(stat)):
        if stat[i][1] > heap[1][1]:
            heap[1] = stat[i]
            sift_down(heap, 1, k+1)
    return [item[0] for item in heap[1:]]


nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))
