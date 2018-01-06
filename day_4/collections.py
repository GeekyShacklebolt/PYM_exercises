#!/usr/bin/env python3

# collections module

from collections import Counter
import re
path = '/usr/share/doc/python2.7/copyright'
words = re.findall('\w+',open(path).read().lower())
Counter(words).most_common(10)

# elements function: returns an iterator
c = Counter('shiva' = 4, 'saxena' = 5, 'learning' = 3)
print(list(c.elements())

# also

Counter('alkjalskdfalsgh').most_common(4)

# defaultdict

from collections import defaultdict
s = [('shiva',9),('saxena',7),('shiva',4),('saxena',2)]
d = defaultdict(list)
for i,j in s:
    d[i].append(j)

d.items()

# namedtuple

from collections import namedtuple
Name = namedtuple('Name',['Real','Nick'])
obj = Name(Real = 'Shiva Saxena', Nick = 'GeekyShacklebolt')
print(obj)
print(obj.Real,' ',obj.Nick)
a, b = obj
print(a,' ',b)
