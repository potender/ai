# def fun(n):
#     ret = 1
#     for i in range(1,n+1):
#         ret *= i
#     return ret
#
# print(fun(20))


#正方形面积
# def area_square(n):
#     return n*n
#
# n = int(input("输入正方形的边长："))
# print("正方形的面积" + str(area_square(n)))

#位置参数
# def Print(x, y, z):
#     print(x, y, z)
# Print(1,2,3)

#关键字参数
# def Print(x, y, z):
#     print(x,y,z)
# Print(y=1, z=2, x=3)
# Print(1, y=3, z=2)

#默认参数
# def registor(name, age, sex="male"):
#     print(name, age, sex)
#
# registor("li",12)
# registor("li",12,"female")

# #参数可选
# def Name(last_name, first_name, mid_name=None):
#     if mid_name:
#         return first_name+mid_name+last_name
#     else:
#         return first_name+last_name
#
# name1 = Name("li","xiao","lan")
# name2 = Name("li","xiao")
#
# print(name1)
# print(name2)

#可变长参数*args
# def fun(x,y,z,*args):
#     print(x, y, z)
#     print(args)
#
# fun(1,2,3,4,5,6)

#全局变量——函数体内直接用
# n = 3
# arr = [0]
# def mul(x, y):
#     global z
#     z = n*x*y
#     arr.append(z)
#     return z
#
# ret = mul(3,5)
# print(ret)
# print(z)
# print(arr)

#多个返回值
# def fun(x):
#     return x,x*x,x**3
#
# print(fun(3))
# a,b,c = fun(2)
# print(a)
# print(b)
# print(c)

#匿名函数————sort,max,min
arr = [(23,32),(12,21),(56,65)]
arr.sort(key = lambda x: x[1],reverse=True)
print(arr)
a = max(arr,key = lambda x:x[1])
print(a)