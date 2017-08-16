def f(x):
    # 一个形参
    return x * x


def rf(x, y):
    # 两个形参
    return x * y


# map 函数参数仅接受 1 个参数，一元操作函数
m = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(m))

# python3 中 reduce 已不再是内建函数，需 import
from functools import reduce
# reduce 函数参数必须有 2 个形参，二元操作函数
r = reduce(rf, [1, 3, 5, 7, 9])
print(r)