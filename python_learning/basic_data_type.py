# #不同进制
# n=16==0b10000==0o20==0x10
# print(n)
#
# a=bin(16)
# b=oct(16)
# c=hex(16)
# print(a,b,c)
#
# d=int(a,2)
# e=int(b,8)
# f=int(c,16)
# print(d,e,f)

# #round四舍五入
# a=1.234
# b=round(a,2)
# print(b)

#复数
# 3+2j 2+1j

#乘方**
# print(2**3)

#运算空格
# print(1 + 2 - 3*4)

#整数商与取模
# print(13//3,13%3)

#function
# print(abs(-5))
# print(abs(3+4j))
# print(pow(2,3))
# print(pow(2,4,3))
# print(divmod(13,5))
# print(max(1,2,3,4,5,6))
# print(min(1,2,3,4))
# print(sum((1,2,3,4,5)))

#借助库numpy或math
# import math
# print(math.exp(2))
# print(math.sqrt(2))

# #字符串
# print("I'm a student")
# print('"happy" is a interesting thing')
# print("\"happy\" is a interesting thing")

#转移换行
# s="py\
# thon"
# print(s)

#索引
# s="0123456789"
# print(s[2])
# print(s[-1])

# #字符串切片
# s="0123456789"
# print(s[0:9:2])
# print(s[::-1])

#成倍复制
# a="I love her"
# print(a*3)

#成员运算
# a="I love her"
# t="her" in a
# print(t)
# for s in a:
#     print(s)
# n=len(a)
# print(n)

#ord and chr
# print(ord("嘿"))
# print(chr(123))

#字符串分割——split
# language="c c++ c# python java"
# language_list=language.split(" ")
# print(language)
# print(language_list)
#
#字符串聚合——join
# s="123456"
# s_join = " ".join(s)
# print(s)
# print(s_join)
#
# s1=["1","2","3"]
# s_join1="*".join(s1)
# print(s1)
# print(s_join1)

#删除两端或一端字符
# s="11111I love her.11111"
# print(s)
# print(s.strip("1"))
# print(s.lstrip("1"))
# print(s.rstrip("1"))

#字符串替换
# s="i love wang"
# s1=s.replace("wang","her")
# print(s)
# print(s1)

#统计字母个数
# s="1234567891234364314"
# print("1:",s.count("1"),"个")

#字符大小写upper，lower,title
# s="I Love Her"
# print(s.upper())
# print(s.lower())

# s="i love her"
# print(s.title())

# print(any([1,0,None,False]))

#布尔运算
# age=20
# print(type(age))

#