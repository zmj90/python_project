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
