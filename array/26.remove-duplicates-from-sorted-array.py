def removeDuplicates(nums):
    for n in nums[:]:
        if nums.count(n) > 1:
            nums.remove(n)
    return len(nums)
