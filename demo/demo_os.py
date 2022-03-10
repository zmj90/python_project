import os


path = os.getcwd()
print(path, type(path))
# D:\doing\study\demo\python_project\demo <class 'str'>
# os.system("dir")
print(__file__, type(__file__))
# D:\doing\study\demo\python_project\demo\demo_os.py <class 'str'>
print(dir())
# for i in dir():
#     print(eval(i))
print(eval('__import__("os").system("dir")'))

