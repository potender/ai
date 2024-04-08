import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]
# plt.plot(x, y)
# # plt.ylabel("squares")
# # plt.show()


"""折线图"""
# x = np.linspace(0, 2*np.pi, 100)
# # plt.plot(x, np.sin(x))
# # plt.plot(x, np.cos(x))
# plt.show()

# offsets = np.linspace(0, np.pi, 5)
# colors = ["blue", "g", "r", "yellow", "pink"]
# for offset, color in zip(offsets, colors):
#     plt.plot(x, np.sin(x-offset), color=color)
# plt.show()

# x = np.linspace(0, 10, 11)
# offsets = list(range(8))
# linestyles = ["-", "--", "-.", ":"]
# for offset, linestyle in zip(offsets, linestyles):
#     plt.plot(x, x+offset, linestyle=linestyle)

# offsets = list(range(0, 12, 3))
# linewidths = (i*2 for i in range(1, 5))
# for offset, linewidth in zip(offsets, linewidths):
#     plt.plot(x, x+offset, linewidth=linewidth)

# markers = ["*", "+", "o", "s"]
# for offset, marker in zip(offsets, markers):
#     plt.plot(x, x+offset, marker=marker, ms=10)

# plt.show()


# x = np.linspace(0, 2*np.pi, 100)
# plt.plot(x, np.sin(x))
# plt.xlim(-1, 7)
# plt.ylim(-1.5, 1.5)
# plt.axis("equal")

# x = np.logspace(0, 5, 100)
# plt.plot(x, np.log(x))
# plt.xscale("log")

# x = np.linspace(0, 10, 100)
# plt.plot(x, x**2)
# plt.xticks(np.arange(0, 12, step=1), fontsize=15)

# x = np.linspace(0, 2*np.pi, 100)
# plt.plot(x, np.sin(x), "b-", label="Sin")
# plt.plot(x, np.cos(x), "b--", label="Cos")
# plt.title("A Sin Curve", fontsize=20)
# plt.xlabel("x", fontsize=15)
# plt.ylabel("sin(x)", fontsize=15)
# plt.legend(loc="upper center", frameon=True, fontsize=15)
#
# x = np.linspace(0, 2*np.pi, 100)
# plt.plot(x, np.sin(x), "b-")
# plt.text(3.5, 0.5, "y=sin(x)", fontsize=15)
#
# plt.show()

"""散点图"""
# x = np.linspace(0, 2*np.pi, 20)
# plt.scatter(x, np.sin(x), marker="o", s=30, c="r")
# plt.show()


"""柱形图"""
#简单柱形图
# x = np.arange(1, 6)
# plt.bar(x, x*2, align="center", width=0.5, alpha=0.5, color='yellow', edgecolor='red')
# plt.xticks(x, ('G1', 'G2', 'G3', 'G4', 'G5'))
# plt.show()

#颜色，x标签
# x = ["G" + str(i) for i in range(5)]
# y = 1 / (1 + np.exp(-np.arange(5)))
# colors = ['red', 'yellow', 'blue', 'green', 'gray']
# plt.bar(x, y, align="center", width=0.5, alpha=0.5, color=colors)
# plt.show()

#累加柱形图
# x = np.arange(5)
# y1 = np.random.randint(20, 30, size=5)
# y2 = np.random.randint(20, 30, size=5)
# plt.bar(x, y1, width=0.5, label="man")
# plt.bar(x, y2, width=0.5, bottom=y1, label="woman")
# plt.legend()
# plt.show()

#并列柱形图
# x = np.arange(15)
# y1 = x+1
# y2 = y1+np.random.random(15)
# plt.bar(x, y1, width=0.3, label="man")
# plt.bar(x+0.3, y2, width=0.3, label="woman")
# plt.legend()
# plt.show()

#横向柱形图
# x = ['G1', 'G2', 'G3', 'G4', 'G5']
# y = 2 * np.arange(1,6)
# plt.barh(x, y, align="center", height=0.5, alpha=0.8, color="blue", edgecolor="red")
# plt.show()


"""多子图"""
#简单多子图
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
# t1 = np.arange(0, 5, 0.1)
# t2 = np.arange(0, 5, 0.02)
# plt.subplot(211)
# plt.plot(t1, f(t1), "bo-", markerfacecolor="r", markersize=5)
# plt.title("A tale of 2 subplots")
# plt.ylabel("Damoed os")
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), "r--")
# plt.xlabel("time(s)")
# plt.ylabel("undamped")
# plt.show()


"""直方图"""
mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)
plt.hist(x, bins=50, facecolor='r', alpha=0.75)
plt.show()



















































