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
# print(eval('__import__("os").system("dir")'))

l1 = os.listdir(os.getcwd())
l2 = os.listdir(".")
# 功能： 查看文件列表, 参数： 指定目录, 返回值：目录中的文件名列表
print(l1, type(l1))
print(l2, type(l2))

# os.remove(file)
# 功能： 删除文件, 参数： 指定文件
