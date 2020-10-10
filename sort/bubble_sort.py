# 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
# 针对所有的元素重复以上的步骤，除了最后一个；
# 重复步骤1~3，直到排序完成


def BubbleSort(lst):

    if len(lst) <= 1:
        return lst

    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                (lst[j], lst[j + 1]) = (lst[j + 1], lst[j])  # 其实就是一轮轮把最大的元素排到最后

    return lst


input = [2, 1, 3, 4, 1]
output = BubbleSort(input)


print(output)