#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 注意：
# input 返回的是字符串
# 必须通过int()转换成整数
# 才能用于数值比较
age = int(input('Input your age:'))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#============BMI指数计算====================
# BMI = 体重(kg)除以身高(m)的平方
height = int(input('输入你的身高(cm)：'))
weight = int(input('输入你的体重(kg)：'))

BMI = weight * 10000/ (height * height)
print('你的BMI指数是:%.1d，评价为：' % BMI)
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('超重')
else:
    print('严重肥胖')
