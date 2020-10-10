# 输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据包括多组。

import sys

for line in sys.stdin.readlines():  # 不指定一共有多少行，一直读取到没有
    a = line.split()  # 这里转化为二维数组
    print(int(a[0]) + int(a[1]))  # 注意读取的是str，需要转化为int


# 输入数据包括多组。
# 每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
# 接下来n个正整数,即需要求和的每个正整数。

# 读取多行输入，同时每行的元素数量不定

import sys

for line in sys.stdin.readlines():  # 不指定一共有多少行，一直读取到没有
    a = line.split()  # 这里转化为二维数组
    a = list(map(int, a))  # 因为input()的list都是str，要转为int
    if a[0] == 0:
        break

    print(sum(a[1:]))  # 注意读取的是str，需要转化为int

# 以上都是针对没有指定输入行数的情况，如果有指定其实也可以用上面的代码，都一样
