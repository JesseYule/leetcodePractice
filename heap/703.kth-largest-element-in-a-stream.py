from heapq import *


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapify(self.nums)
        while len(self.nums) > self.k:  # cut heap to size:k
            heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heappush(self.nums, val)
            heapify(self.nums)  # cation
        else:
            top = float('-inf')
            if len(self.nums) > 0:
                top = self.nums[0]
            if top < val:
                heapreplace(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

