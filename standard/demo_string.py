"""
https://docs.python.org/zh-cn/3/library/string.html
"""

import string

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(f"sadas{string.digits:*^30}asdasd")
# print(string.whitespace.__str__())
print(string.whitespace.__repr__())
