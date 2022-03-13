import os.path as path


p = path.abspath("py.py")
p1 = path.abspath(__file__)
print(p)
# D:\doing\study\demo\python_project\demo\py.py
print(p1)
# D:\doing\study\demo\python_project\demo\demo_os_path.py
p2 = path.basename(__file__)
print(p2)
# demo_os_path.py
p3 = path.dirname(__file__)
print(p3)
# D:\doing\study\demo\python_project\demo
p4 = path.join(p3, p2)
print(p4)
# D:\doing\study\demo\python_project\demo\demo_os_path.py
p5 = path.split(p4)
print(p5)
# ('D:\\doing\\study\\demo\\python_project\\demo', 'demo_os_path.py')

f1 = path.getsize(__file__)
# 功能： 获取文件大小, 参数： 指定文件, 返回值： 文件大小
print(f1, type(f1))

# path.exists(file)
# 功能： 查看文件是否存在, 参数： 指定文件, 返回值：存在返回True，不存在返回False

# path.isfile(file)
# 功能： 判断文件类型, 参数： 指定文件, 返回值：普通文件返回True，否则返回False

