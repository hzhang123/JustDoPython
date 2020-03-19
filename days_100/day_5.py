# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  day_5.py
@CreateTime     :  2020/3/19 20:29
------------------------------------
"""

print('----- 最简单函数示例 -----')

def hello():
    print('hello world')


hello()

print('----- 加减乘除 -----')

def add(a, b):
    return a + b


def reduce(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print(add(1, 2))
print(reduce(3, 4))
print(multiply(4, 5))
print(divide(4, 3))

print('----- 返回多个值 -----')

def more(x, y):
    nx = x + 2
    ny = y + 3
    return nx, ny
x, y = more(1, 2)
print(x, y)

print('----- 递归函数 -----')

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(f'递归{fact(6)}')

