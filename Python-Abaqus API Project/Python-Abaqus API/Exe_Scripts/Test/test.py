import os
import sys
from datetime import datetime

### Print the current dic ###

base_dir1 = os.path.dirname(__file__)
base_dir2 = os.getcwd()
print(base_dir1)
print(base_dir2)
sys.path.append('..') #回到上层目录
base_dir3 = os.getcwd()
print(base_dir3)
# os.path.dirname   =>   /xx/xx，os.getcwd()    =>  \xx\xx，

# C:\Users\jiaor\PycharmProjects\pythonProject_HP\Python-Abaqus API Project\Python-Abaqus API\Exe_Scripts\Test

# whether the path exists
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        print("---  创建新的文件夹...  ---")
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  OK  ---")
    else:
        print("---  文件夹已存在!  ---")
mkdir(base_dir2)
# Obtaining the parent directory
# for the result folder name
import sys
print("abs path is %s" %(os.path.abspath(sys.argv[0])))
print(sys.argv[0])
print(sys.argv) # 输入参数列表
print(sys.argv[0])  # 第0个就是这个python文件本身的路径（全路径）
print(os.path.basename(sys.argv[0]))  # 当前文件名名称
print(os.path.basename(__file__))  # 当前文件名名称
a = os.path.basename(sys.argv[0])
a = a[:-3]
print(a)

time1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time2 = datetime.now().strftime("%Y%m%d%H%M")
print(time1,time2)
# find the direct result directionary



