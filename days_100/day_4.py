# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  day_4.py
@CreateTime     :  2020/3/19 13:06
------------------------------------
"""


print('-----if 语句-----')
# if 判断:
#     执行语句
# else:
#     执行语句

x = -2
if x < 0:
    x = 0
    print('小于0')
elif x == 0:
    print('等于0')
else:
    print('大于0')


print('-----for 循环-----')

for letter in 'hzhang':
    print(f'当前字母:{letter}')

fruits = ['banana', 'mongo', 'apple']
for fruit in fruits:
    print(f'当前水果:{fruit}')

# 通过索引
for index in range(len(fruits)):
    print(f'索引-当前水果:{fruits[index]}')


print('-----while 语句-----')

count = 0
while (count < 3):
    print(f'this count is: {count}')
    count += 1
else:
    print(f'else count is:{count}')


print('-----break 用法-----')

for letter in 'youkonw':
    if letter == 'o':
        break
    print(f'当前字母为：{letter}')


print('-----continue 用法-----')

for letter in 'youkonw':
    if letter == 'o':
        continue
    print(f'当前字母为：{letter}')

print('-----pass 空语句-----')
if True:
    pass
