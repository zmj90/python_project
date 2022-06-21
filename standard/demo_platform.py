import platform

v1 = platform.python_version()
print(v1, type(v1))
# 3.9.6 <class 'str'>
v2 = platform.version()
print(v2, type(v2))
# 10.0.19042 <class 'str'>
