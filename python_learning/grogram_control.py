# a = 1
# b = 2
# c = 3
# print(a > b)

# a=[1]
# if a:
#     print("非空")
# else:
#     print("空")

# print((a > b) or not(b < c))

# num=[1, 2, 3, 4]
# print(2 not in num)

#条件语句
# age = 2
# is_pub = 0
# if age < 8:
#     print("年龄小于八")
#     if is_pub == 1:
#         print("can")
#     else:
#         print("cannot")
# elif age < 16:
#     print("年龄八到十六")
# elif age < 32:
#     print("年龄十六到三十二")
# else:
#     print("年龄很大")
#
# s = ["qwe", "asd", "qwe"]
# for i in s:
#     print(i)

# a = {"10":"qwe", "11":"asd"}
# for i in a.keys():
#     print(i)
#
# res=[]
# for i in range(4):
#     res.append(i**2)
# print(res)

# product_scores = [71, 72, 78, 93, 49, 20]
# count = 0#不合格数量
# for i in range(len(product_scores)):
#     if product_scores[i] <= 70:
#         count+=1
#         print("产品{}不合格".format(i+1))
#     if count == 2:
#         break
# else:
#     print("产品都合格")

# age = 18
# gress = int(input("输入猜的年龄"))
# while age!=gress:
#     if gress > age:
#        print("猜大了")
#     else:
#         print("猜小了")
#     gress = int(input("输入猜的年龄"))
# else:
#     print("猜对了")

# age = 18
# Flag = True
# while Flag:
#     gress = int(input("输入猜的年龄"))
#     if gress > age:
#        print("猜大了")
#     elif gress < age:
#         print("猜小了")
#     else:
#         print("猜对了")
#         Flag = False
#
# age = 18
# Flag = True
# while Flag:
#     gress = int(input("输入猜的年龄"))
#     if gress > age:
#        print("猜大了")
#     elif gress < age:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break


#输入十以内的奇数
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)

# s = ["qwe","qwe", "asd","zxc"]
# while "qwe" in s:
#     s.remove("qwe")
# print(s)

# not_read = ["qwe", "rty", "asd", "zxc"]
# ok = []
# while not_read:
#     reading = not_read.pop()
#     ok.append(reading)
#     print("我已经读了{}".format(reading))
# print(ok)

#封装条件判断
number = (1, 2, 3, 4, 5)
def judge(num):
    a,b,c,d,e = num
    x = a < b
    y = b < c
    z = not e
    return x and y or z
if judge(number):
    print("yes")
else:
    print("no")
    