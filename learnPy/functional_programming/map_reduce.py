def f(x):
    # 一个形参
    return x * x


def rf(x, y):
    # 两个形参
    return x * y


# map 函数参数仅接受 1 个参数
m = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(m))

from functools import reduce
# reduce 函数参数需有s两个形参
r = reduce(rf, [1, 3, 5, 7, 9])
print(r)