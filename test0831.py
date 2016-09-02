#!/usr/bin/env python
#coding:utf-8


import re
str = 'python1班'

print(re.search(r'(\w+)(\d)', str).group(0))
print(re.search(r'(\w+)(\d)', str).group(1))
print(re.search(r'(\w+)(\d)', str).group(2))







# list1 = ['clinux','cpython']
# 
# 
# print('wode','nide',[x for x in list1])