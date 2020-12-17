import numpy as np
import sys
import time
# numpy take less memory then array
i = range(1000)
print(sys.getsizeof(5)*len(i))

array = np.arange(1000)
print(array.size*array.itemsize)


# numpy speed

SIZE = 10000000
l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print('python list time :-',(time.time()-start)*1000)

start = time.time()
result = a1+a2
print('numpy result time',(time.time()-start)*1000)
