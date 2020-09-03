def twoSum(nums, target):
    result = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target and i != j:
                result = [i, j]
    return result
