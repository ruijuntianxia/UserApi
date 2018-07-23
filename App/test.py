#Author by Andy
#_*_ coding:utf-8 _*_
#__file__获取当前程序的相对路径
import os,sys
#print(__file__)
# os.path.abspath(__file__) 获取当前程序的绝对路径
print(os.path.abspath(__file__))
# E:\my python study\day4\Atm\bin\atm.py
Path=os.path.abspath(__file__)
# print(os.path.dirname(Path))获取当前程序的父目录的绝对路径
BASE_DIR=os.path.dirname(os.path.dirname(Path))
print(BASE_DIR)
# E:\my python study\day4\Atm
#将BASE_DIR添加到系统环境变量中
sys.path.append(BASE_DIR)

from Apis import LoginCheck

print('OK')

