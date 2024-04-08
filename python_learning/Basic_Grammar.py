# #列表
# a=[1,2,3]
# print(a)
# print(a[0])
#
# #元组
# b=(1,2,3)
# #b[1]=0 错误
#
# #字典
# student={101:"小明",102:"小红"}
# print(student[101])
# #print(student["小明"]) 错误
#
# #集合
# s={"li","wang","li"}
# print(s)
#
# #变量
# Python_第1=1
# print(Python_第1)
#
# #交换
# x,y=1,2
# print(x, y)
# x,y=y,x
# print(x,y)
#
# #实现1+到5
# ret=0
# for i in [1,2,3,4,5]:
#     ret+=i
# print(ret)
#
# i=1
# ret=0
# while i<=5:
#     ret+=i
#     i+=1
# print(ret)
#
# #条件语句
# age=44
# if age>=22:
#     print("能结婚")
# else:
#     print("不能结婚")

# 输入
# x=input("请输入一个数字：")
# y=input()
# print(x + y)

# x=eval(input("请输入数字"))
# y=eval(input("请输入数字"))
# print(x + y)

#不换行
# print(123,end=" ")
# print(456)

#格式化输出
a=123123.123
b=456456.456
print("a={0},b={1}".format(a,b))
#填充
print("{0:_^20}".format(a))
#千分位分隔符
print("{0:,}".format(a))
#留小数
print("{0:.2f}".format(a))
#百分数
print("{0:.1%}".format(a))
#科学计数法
print("{0:.2e}".format(a))

