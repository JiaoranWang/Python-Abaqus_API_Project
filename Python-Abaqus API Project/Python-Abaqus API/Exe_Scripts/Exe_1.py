import os
from Test_Environment import Students  # School是文件名称，Students为模块名称，Student为类名称
os.chdir(r"C:\Users\jiaor\PycharmProjects\pythonProject_HP\Python-Abaqus API Project\Python-Abaqus API")

stu1 = Student("张三", "云南")  # 传入参数
stu1.speak()  # 调用方法

