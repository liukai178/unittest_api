##打印列表元素及索引
# d = ['a','b','c']
# for i in enumerate(d):
#     print(i)

##进度条
# from tqdm import tqdm
# import time
# for i in tqdm(range(10000)):
#     time.sleep(0.01)


##将字符串/数字拆开并拼接成一个列表(itertools.chain)
# import itertools
##列表工具itertools
# a = list(itertools.chain('wdfg',range(10)))
# print(a)


#1到10的阶乘
import itertools
import operator
# a = list(itertools.accumulate(range(10)))
#每隔一个数字递增加1
# a = list(itertools.accumulate(range(1,11),operator.mul))
#从1开始阶乘
# print(a)


# #打印目录下的所有文件
# import os
##先用os.walk包装目录
# d = os.walk(r'F:\guoyou\U盘\Desktop\liukai\liukai\testcases')
# for dd in d:
#     print(dd)

