# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-20,00:30 
# python 3.8.2


from functools import reduce

# 需求1：对列表中所有的数值求平方
list1 = [0, 1, 2, 3, 4]
def square(x):
    return x*x 

# # 普通方案：
ans1 = []
for i in list1:
    ans1.append(i*i)
# print(ans1)

# # map方案
ans_map = map(square, list1)
for i in ans_map:
    print(i)


# 需求2：返回列表中的所有奇数
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(x):
      return x & 1 != 0
# # 普通方案：
ans2 = []
for i in list2:
    if is_even(i):
        ans2.append[i]

# # filter方案
ans_filter = filter(is_even, list2)
for i in ans_filter:
    print(i)


# 需求3：求列表中的所有数的和
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def mysum(x,y):
    return x + y 

# # 普通方案：
# 你会发现，如果不用sum函数，你连这个都很难优雅的写出来

# # reduce方案：
ans_reduce = reduce(mysum, list3)
print(ans_reduce)

