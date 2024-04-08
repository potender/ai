import copy

import my_numpy

# list_1 = [1, [2, 3], (4, 5), {"haha": "ads"}]
# list_2 = list_1.copy()
# print(list_1)
# print(list_2)
#
# list_1.append(100)
# print(list_1)
# print(list_2)
#
# list_1[1].append(100)
# print(list_1)
# print(list_2)

# list_2 = copy.deepcopy(list_1)
# list_2[1].append(100)
# print(list_1)
# print(list_2)

# x = 1
# y = "python"
# print("x id:", id(x))
# print("y id:", id(y))
# x +=2
# y +="2"
# print("x id:", id(x))
# print("y id:", id(y))

#删除列表特定元素
arr = ["a", "a", "a", "w", "1", "a", "a", "123"]
x = "a"
for i in range(-len(arr), 0):
    if arr[i] == x:
        arr.remove(arr[i])
print(arr)

#解析语法
# arr = [i**3 for i in range(10) if i%2 == 0]
# print(arr)

# x = [1, 2, 3]
# y = [3, 2, 1]
# arr = [i*j for i, j in zip(x, y)]
# print(arr)

#字符串合并
# colors = ["black", "white"]
# sizes = ["S", "L"]
# # cloth = ["{} {}".format(color, size) for color in colors for size in sizes]
# cloth = ["{} {}".format(color, size) for color, size in zip(colors, sizes)]
# print(cloth)

#字典的解析语法
# arr = {i: i**3 for i in range(11) if i%2 == 0}
# for k, v in arr.items():
#     print(k, ': ', v)
#
# squares = (i**2 for i in range(5))
#
# #条件表达式
# a = -1
# x = a if a >= 0 else -a
# print(x)
