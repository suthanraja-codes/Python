
# Reduce (function , iterable) - performs function on first two elements and repeats is until
# one value remains on the iterable.

import functools
# val = [4,7,8,3]
# s = functools.reduce(lambda x,y:x+y,val)
# print(s)


chars = ['s','u','t','h','a','n']
s =functools.reduce(lambda x,y:x+y,chars)
print(s)