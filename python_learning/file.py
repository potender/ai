# with open("text.txt", "r", encoding="utf-8") as f:

    #read()
    # text = f.read()
    # print(text)

    #readline()
    # for i in range(3):
    #     text_line = f.readline()
    #     print(text_line)

    #不知道多少行
    #不用
    # while True:
    #     text = f.readline()
    #     if not text:
    #         """读到结尾了"""
    #         break
    #     else:
    #         print(text, end="")

    #用
    # for text in f:
    #     print(text, end="")


    #textlines
    # textlines = f.readlines()
    # print(textlines)

# #文件的写如入
# with open("text.txt", "w", encoding="utf-8") as f:
#     f.write("从前初识这世界\n")
#     f.write("万般留恋\n")
#     f.write("看着天边似在眼前\n")
#
# with open("text.txt", "a", encoding="utf-8") as f:
#     f.write("也甘愿赴汤蹈火去走他一遍\n")

#r+
# with open("text.txt", "r+", encoding="utf-8") as f:
#     f.seek(0, 2)
#     f.write("lalala")

#try_except
# x = 0
# y = 10
# try:
#     z = y/x
# except ZeroDivisionError:
#     print("0不能做除数")
# except IndexError:
#     print("索引错误")
#
# print("程序正常执行")

Ex = []
a = {"name": "wang"}
try:
    print(a["age"])
except Exception:
    print("出错1")
    