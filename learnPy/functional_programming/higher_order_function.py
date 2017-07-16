from math import sqrt
from math import tan
import builtins
'''
高阶函数应用，返回一个数字不同方法计算结果
'''

'''
description: 对 num 做运算，结果输出到以 *kw 名称为 key 的字典中
parameters:
    num: 变量，只支持 int, float。
    *kw：函数头指针，可输入多个并行执行函数
'''
def same(num, *kw):
    # 参数类型检查
    # num 是否为 int，float
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')

    # 初始化结果字典
    rel = {}
    # 循环计算可变参数
    for func in kw:
        try:
            # func 被定义为函数，用 .__name__ 取string类型的函数名，直接打印取到的是函数注释
            rel[func.__name__] = func(num)
        except ValueError:
            # except 类似 java 的 catch，不过 except 更形象
            # str(func)[str(func).find('function ') + 9:-1] 为 func.__name__ 的迂回实现
            # str(func) 结果为：‘<built-in function abs>’
            # find('function ') 定位到‘f’的位置为10
            rel[str(func)[str(func).find('function ') + 9:-1]] = 'None'
    # 返回结果字典
    return rel


result = same(-10.5, sqrt, abs, tan)
print(result)

'''
函数式编程简单例程
'''
def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))