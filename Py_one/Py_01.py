#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：

# 一个打印
print(22 + 22)

# python 中 true false 首字母大写 严格区分大小写
print(True)
print(False)

# 多行打印
print('''line1
line2
line3''')

# and 与运算 等价于 &&
print(True and True)
# or 或运算 等价于 ||
print(True or False)
# not 非运算 等价于 !
print(not True)

# if判断 : 缩进符
if 125 > 18:
    print('正确')
else:
    print('错误')

# 常量就是不能变的变量 比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）
PI = 3.14159265359
print(PI)

# 算法符号 / 正常除号  // 地板除 不管除得尽除不尽都返回整数  % 求余
print(10 // 3)
