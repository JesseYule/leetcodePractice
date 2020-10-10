import heapq as hq
import numpy as np

data = np.arange(10)
np.random.shuffle(data)

heap = []

for i in data:
    hq.heappush(heap, i)  # 得到最小堆

print(heap)
min = hq.heappop(heap)  # pop出最小值，注意此时数组里已经没了这个值了
print(heap)

# 直接处理list得到最小堆

heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
hq.heapify(heap)

# ---------注意，heapq对最大堆支持不是很好，比如使用heappush后得到的不是就不是最大堆了
# 但是我们依然可以创建最大堆和进行pop操作

data = [1,5,3,2,8,5]
hq._heapify_max(data)
print(data)
print(hq._heappop_max(data))
print(data)
hq._heapreplace_max(data, 12)
print(data)
hq.heappush(data, 15)
print(data)

# 从上述的函数就可以看出heapq主要针对最小堆进行分析


