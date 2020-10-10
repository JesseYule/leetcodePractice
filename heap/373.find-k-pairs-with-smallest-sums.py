import heapq
import itertools

# 不计算整个矩阵，而将每一行变成三元组[u + v，u，v]的生成器，仅在要求计算下一行时才计算下一行，
# 然后将这些生成器与堆合并。 占用 O(m + k * log(m))O(m+k∗log(m)) 的时间复杂度和 O(m)O(m) 的空间复杂度。


def kSmallestPairs(nums1, nums2, k):
    streams = map(lambda u: ([u + v, u, v] for v in nums2), nums1)
    stream = heapq.merge(*streams)  # 将多个已排序的输入合并为一个已排序的输出

    return [suv[1:] for suv in itertools.islice(stream, k)]


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3

print(kSmallestPairs(nums1, nums2, k))

