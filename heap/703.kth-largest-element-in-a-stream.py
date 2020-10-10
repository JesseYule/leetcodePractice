from heapq import *


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapify(self.nums)  # 注意，这里默认得到最小堆，原地操作
        while len(self.nums) > self.k:

            #  这一步十分巧妙，虽然默认构建最小堆，但仍然可以通过最小堆计算出第k大的元素，也可以计算出第k小的元素
            # 要么pop k次，要么pop到只剩k个元素

            heappop(self.nums)  # 这里pop的是堆中最小的元素，一直pop直至堆的尺寸等于k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:  # 这里主要处理len小于k的情况，直接输出最小值就好
            heappush(self.nums, val)
            heapify(self.nums)
        else:
            # 正常情况add一个元素，其实主要就是判断需不需要替换堆顶元素
            top = float('-inf')
            if len(self.nums) > 0:
                top = self.nums[0]  # 这是堆中的最小元素
            if top < val:
                heapreplace(self.nums, val)  # 替换堆顶元素，如果val更小则不需要
        return self.nums[0]  # 返回堆的最小元素，即为第k大的元素

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

