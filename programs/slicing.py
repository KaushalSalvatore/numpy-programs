import numpy as np
a = np.array([[1,3,4],[1,3,4],[1,3,4]])

print(a[0:2])

print(a[-1])

print(a[1,2])

print(a[0:2,2])

for row in a:
    print(row)

a1 = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print(a1,b)
print(np.vstack((a1,b)))
print(np.hstack((a1,b)))

c = np.arange(30).reshape(2,15)
print(c)

print(np.hsplit(c,3))
print(np.vsplit(c,2))

b= a1>4
print(b)

print(a1[b])

