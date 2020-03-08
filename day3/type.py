import sys
print(sys.getrefcount(3))
print(type(3))
a = 3
print(sys.getrefcount(3))
print(type(a))
b = 3
print(sys.getrefcount(a))
print(a is b)
