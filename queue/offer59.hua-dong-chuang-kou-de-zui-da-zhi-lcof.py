def maxSlidingWindow(nums, k):

    if nums == []:
        return []

    output = []
    for i in range(len(nums) - k + 1):
        output.append(max(nums[i:i+k]))

    return output
