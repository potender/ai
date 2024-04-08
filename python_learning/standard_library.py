#time

import time
# t_local = time.localtime()
# t_UTC = time.gmtime()
# print(t_local)
# print(t_UTC)
#
# print("ctime:", time.ctime())

# t_1_start = time.time()
# t_2_start = time.perf_counter()
# t_3_start = time.process_time()
# # print(t_1_start)
# # print(t_2_start)
# # print(t_3_start)
#
# ret = 0
# for i in range(100000):
#     ret +=i
# time.sleep(2)
#
# t_1_end = time.time()
# t_2_end = time.perf_counter()
# t_3_end = time.process_time()
# print("time:{}".format(t_1_end - t_1_start))
# print("time.perf_counter:{}".format(t_2_end - t_2_start))
# print("time.process_time:{:.5f}".format(t_3_end - t_3_start))

# lctime = time.localtime()
# print(time.strftime("%Y-%m-%d %A %H:%M:%S", lctime))


#random
from random import *
import matplotlib.pyplot as plt
# seed(100)
# print(random())
# arr = [randrange(0, 10, 2) for i in range(10)]
# print(arr)
# arr = [random() for i in range(5)]
# print(arr)
# arr = [uniform(2.1, 3.5) for i in range(5)]
# print(arr)
# print(choice(["win", "lose", "draw"]))
# print(choice("qwertyuiop"))
# print(choices(["win", "lose", "draw"], [4, 4, 2], k=5))
# numbers = ['one', 'two', 'three', 'four']
# shuffle(numbers)
# print(numbers)
# print(sample(numbers, k=3))

# num = [gauss(0, 1) for i in range(100000)]
# plt.hist(num, bins=1000)
# plt.show()


#collection
import collections
#具名元组namedtuple
# Point = collections.namedtuple("Point", ["x", "y"])
# p = Point(x=1, y=2)
# print(p.x)
# print(p[0])
# m, n = p
# print(m)

# Card = collections.namedtuple("Card", ["rank", "suit"])
# ranks = [str(n) for n in range(2, 11)] + list("JQKA")
# suits = "spades diamonds clubs hearts".split()
# print("ranks:", ranks)
# print("suits", suits)

# cards = [Card(rank, suit) for rank in ranks for suit in suits]
# # print(cards)
# print(choice(cards))
# print(sample(cards, k=5))

# Counter计数器
from collections import Counter
# s = "牛奶奶找刘奶奶买牛奶"
# colors = ['blue', 'red', 'black', 'red', 'blue', 'blue']
# cnt_s = Counter(s)
# cnt_color = Counter(colors)
# print(cnt_s)
# print(cnt_color)
# print(cnt_color.most_common(2))
# print(list(cnt_s.elements()))

# c = Counter(a=3, b=1)
# d = Counter(a=1, b=2)
# print(c+d)

# cards = Counter(tens=16, low_cards=36)
# # print(list(cards.elements()))
# seen = sample(list(cards.elements()), k=10)
# print(seen)
# print(seen.count("tens")/10)


#双向队列deque
# from collections import deque
# d = deque('cde')
# print(d)
# d.append('f')
# print(d)
# d.appendleft("b")
# print(d)
# d.pop()
# print(d)
# d.popleft()
# print(d)


import itertools

# for i in itertools.product('ABC', '01'):
#     print(i)

# for i in itertools.product('ABC', repeat=3):
#     print(i)

# for i in itertools.permutations('ABCD', 3):
#     print(i)

# for i in itertools.permutations(range(3)):
#     print(i)

# for i in itertools.combinations('ABCD', 3):
#     print(i)

# for i in itertools.combinations(range(3), 3):
#     print(i)

# for i in itertools.combinations_with_replacement(range(3), 3):
#     print(i)

#拉链zip
# for i in zip("ABC", "012456789", "zxc"):
#     print(i)

# for i in itertools.zip_longest("ABC", "012456789", "zxc",fillvalue='?'):
#     print(i)


# for i in itertools.repeat(3, 5):
#     print(i)

# for i in itertools.chain('ABC', [1, 2, 3]):
#     print(i)

# for i in enumerate("Python", start=1):
#     print(i)

