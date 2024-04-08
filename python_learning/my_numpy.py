import numpy as np
import matplotlib

#创建
# x = np.array([1, 2, 3, 4])
# print(x)
# print(type(x))
# print(x.shape)
#
# x = np.array([1, 2, 3, 4], dtype="float32")
# print(x)

# x = np.array([[1, 2, 3], [4, 5, 6]])
# print(x)
# print(x.shape)

# x = np.zeros(5, dtype=int)
# y = np.ones((2, 4), dtype=float)
# z = np.full((3, 5), 8.8)
# print(x)
# print(y)
# print(z)

# x = np.eye(3)
# y = np.arange(1, 15, 2)
# z = np.linspace(0, 1, 4)
# m = np.logspace(0, 9, 10)
# n = np.random.random((3, 3))
# print(x)
# print(y)
# print(z)
# print(m)
# print(n)

# x = np.random.normal(0, 1, (3, 3))
# y = np.random.randint(0, 10, (3, 3))
# print(x)
# print(y)
#
# x = np.array([10, 20, 30, 40])
# print(np.random.permutation(x))
# np.random.shuffle(x)
# print(x)

# x = np.arange(10, 25, dtype=float)
# print(x)
# print(np.random.choice(x, size=(4, 3)))


#性质
# x = np.random.randint(10, size=(3, 4))
# print(x.shape)
# print(x.ndim)
# print(x.size)
# print(x.dtype)

# x1 = np.arange(10)
# print(x1)
# print(x1[1], x1[-2])
# x2 = np.random.randint(0, 20, (2, 3))
# print(x2)
# print(x2[0, 0])

#切片
# x1 = np.arange(10)
# print(x1)
# print(x1[:3])
# print(x1[3:])
# print(x1[::-1])
# x2 = np.random.randint(20, size=(3, 4))
# print(x2)
# print(x2[:2, :3])   #前两行，前三列
# print(x2[:2, :3:2])
# print(x2[::-1, ::-1])

# print(x2[1])    #第1行
# print(x2[:, 2])     #第二列

# x3 = np.random.randint(20, size=(3, 4))
# print(x3)
# # x3[0, 0] = 100
# # print(x3)
#
# x4 = x3[:2, :2].copy()
# print(x4)
# x4[0, 0] = 100
# print(x4)
# print(x3)

#数组变形
# x = np.random.randint(0, 10, (3, 4))
# print(x)
# # print(x.shape)
# # x1 = x.reshape(3, 4)
# # print(x1)
# # x2 = x.reshape(1, x.size)   #(1,x.size)
# # # x2 = x[np.newaxis, :]
# # print(x2)
# # x3 = x.reshape(x.size, 1)
# # print(x3)
# x4 = x.ravel()
# print(x4)
# x4[0] = 100
# print(x)

#数组的拼接
# x1 = np.array([[1, 2, 3], [4, 5, 6]])
# x2 = np.array([[7, 8, 9], [10, 11, 12]])
# x3 = np.hstack([x1, x2])
# x4 = np.vstack([x1, x2])
# print(x3)
# print(x4)

#数组的分裂
# x = np.arange(10)
# print(x)
# x1, x2, x3 = np.split(x, [2, 7])
# print(x1, x2, x3)
# x = np.arange(1, 26).reshape(5, 5)
# print(x)
# print(x[:, :2])

#向量化运算
# x1 = np.arange(1, 6)
# print(x1)
# print(x1+5)
# print(x1**2)

# x2 = np.array([1, -1, 2, -2, 3])
# print(x2)
# print(abs(x2))

# x3 = np.linspace(0, np.pi, 3)
# print(x3)
# print(np.sin(x3))

# x4 = np.array([1, 2, 4, 8])
# print(np.log2(x4))

# x1 = np.array([1, 2, 3, 4, 5])
# x2 = np.array([5, 4, 3, 2, 1])
# print(x1+x2)

# x = np.arange(9).reshape(3, 3)
# print(x)
# print(x.T)
# y = x.T
# print(np.dot(x, y))

#广播
# x1 = np.ones((3, 3))
# x2 = np.arange(3)
# print(x1+x2)

# x1 = np.ones((3, 1))
# x2 = np.arange(3)
# print(x1+x2)

#掩码
# x1 = np.random.randint(100, size=(10, 10))
# print(x1)
# # print(x1 > 50)
# # print(np.sum(x1 > 50))
# print(np.any(x1 > 50))

#花哨索引
# x1 = np.random.randint(10, size=10)
# x2 = np.random.randint(10, size=(3, 4))
# print(x1)
# ind1 = [2, 3, 0]
# ind2 = [1, 2, 0]
# print(x1[ind1])
# print(x2[ind2, ind2])

#通用函数
# x = np.random.randint(20, 50, size=10)
# print(x)
# # y = np.sort(x)
# # print(y)
# # x.sort()
# # print(x)
# # print(x)
# print(np.max(x))
# print(np.min(x))
#
# print(np.argmax(x))
# print(np.argmin(x))

#求和
# x = np.arange(1, 6)
# print(x)
# print(x.sum())

# x = np.arange(6).reshape(2, 3)
# print(x)
# print(np.sum(x, axis=1))
# print(np.sum(x, axis=0))

# x = np.arange(1,6)
# print(x.prod())

x = np.random.normal(0, 1, size=10000)
import matplotlib.pyplot as plt
plt.hist(x, bins=50)
plt.show()
print(np.median(x))
print(x.mean())
print(x.var())
print(x.std())
















