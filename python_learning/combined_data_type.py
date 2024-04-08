#列表
# Is=["python",1983,True,{"her":12}]
# print(Is)
#
# s="人工智能"
# s=list(s)
# print(s)
#
# a=("h","e","l","l","o")
# print(list(a))

#range()
# for i in [1,2,3,4,5]:
#     print(i)

# for i in range(1,5,2):
#     print(i)

# a=list(range(6))
# print(a)

#len
# a=list(range(10))
# print(len(a))

# #索引
# grade=[12,13,14,15]
# print(grade[1])
# print(grade[-1])

#切片
# a=list(range(6))
# print(a[:3])
# print(a[::2])

#列表操作
# a=[1,2]
# b=[3,4]
# print(a+b)
# c=a*3
# print(c)

language=["python","c","c++"]
# language2=["R","c#"]
# print(language)
# language.append("java")
# print(language)
# language.insert(1,"Go")
# print(language)
# language.extend(language2)
# print(language)
# language.pop(2)
# print(language)
# language.remove("Go")
# print(language)
# idx=language.index("c++")
# print(idx)
# language[1]="6"
# print(language)
# print("--------------------")
#
# language_c = language.copy()
# print(language_c)
# language_cc=language[:]
# print(language_cc)

# a=[2,1,4,3,5,3,6,2]
# b=a.copy()
# a.sort()
# print(a)
# # print(b)
# # b1=b.sort(reverse = True)
# # print(b)
# # print(sorted(b))
# # print(b)
# a.reverse()
# print(a)
# for i in a:
#     print(i)


#元组

#打包
# def f(x):
#     return x**2,x**3
# # print(f(2))
#
# #解包
# # a,b=f(3)
# # print(a)
# # print(b)
#
# number=[1,2,3,4]
# name=["李","wang","xie","cheng"]
# a=list(zip(name,number))
# print(a)
# for num,name in a:
#     print(num)
#     print(name)


#字典
# student = {2301:"li", 2302:"wang", 2303:'he'}
# print(student)
# print(len(student))
# print(student[2301])
# #增加
# student[2304] = "zhang"
# print(student)
#删除
# del student[2304]
# print(student)
# print(student.pop(2303))
# print(student)
# print(student.popitem())

#d.get()
# s = "牛奶奶找刘奶奶买牛奶"
# d={}
# print(d)
# for i in s:
#     d[i] = d.get(i, 0)+1
#     print(d)

# student = {2301:"li", 2302:"wang", 2303:'he'}
# print(list(student.keys()))
# print(list(student.values()))
# for k, v in student.items():
#     print((k, v))

# A = {10,11,12,13,14}
# B = {11,13,15,17,19}
# print(A&B)
# print(A|B)
# print(A^B)
# print(A-B)
# A.add(15)
# print(A)
# A.remove(15)
# print(A)
# print(len(A))
# for i in A:
#     print(i)



