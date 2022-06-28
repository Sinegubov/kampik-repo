# Списки
s = []
l = [1, 23, [], {}, '111']
s.append(1)
l.pop(2)
w  = [ x ** 2 for x in range(10)]
odds = [x for x in range(10) if x %2 != 0]
print([x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)])
second = [(x, y) for x in range(1, 5) for y in range(5, 1, -1) if x != y]
print(second)
print(s,l)
print(w)
print(odds)

# Кортежи, Named Tuple

a = [1, 2, 3]
b = (1, 2, 3)

# Именованые кортежи
from collections import namedtuple
Car = namedtuple('Car', 'color speed')
my_car = Car('red', 200)
print(my_car.color, my_car.speed)

# Deeque - двусторонняя очередь
import collections
de = collections.deque([1, 2, 3])
print(de)
de.append(4)
print(de)
de.appendleft(0)
print(de)
de.pop()
print(de)
de.popleft()
print(de)

# Set - множества
s = set()
s = set((1,2,3,4,5))
print(s)
s = set([1,2,3,4,5,6,7])
print(s)
s = {1, 2, 3, 4, 5, "test", ()}
s.add("new test")
s.discard(3) # удаление элемента из множества
print(s)
first_part = set((1,2,3,4,5))
second_part = set((6,7,8,9,10))
print(first_part.union(second_part))
print(first_part.intersection(second_part))

print({s for s in [1, 2, 1, 0]})
print({s**2 for s in [1, 2, 1, 0]})
print({s**2 for s in range(10)})
print({s for s in [1, 2, 3] if s % 2})
print({(m, n) for n in range(2) for m in range(3, 5)})


a = frozenset((1,2,3))

# Словари
d = {} # создание словаря
d = {"a":1, "abc":2}
print(d)
d1 = dict([(1,2), (3,4)])
print(d1)
d.clear()
print(d)
d2 = dict([(1,2), (3,4)])
print(d2[1])
d2[7] = 15
print(d2)
d2[(1,2)] = 123
print(d2)
print(d2.items())
print(d2.keys())
print(d2.values())

d3 = {a: a ** 2 for a in range(7)}
print(d3)

# orderDict

import collections
d0 = collections.OrderedDict(one=1, two=2, three=3)
print(d0)
d0['four'] = 4
print(d0)

from collections import defaultdict
dd = defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Katron')
dd['dogs'].append('Mr Snif')
print(dd['dogs'])