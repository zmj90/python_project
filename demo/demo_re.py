import re

m = re.search('def', 'abcdeffhgfdef')
m.group(0)
print(m)
print(m.group())
print(m.group(0))

a = re.search('a', 'sdgfgderwrsa')
print(a)

print(re.compile(r"as"))
