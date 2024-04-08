import pandas as pd
import numpy as np

"""新建"""
# data = pd.Series([1.5, 3, 4.5, 6])
# print(data)
# data1 = pd.Series([1, 3, 4, 6], index=['a', 'b', 'c', 'd'])
# print(data1)
# data2 = pd.Series([1.5, 3, 4.5, 6], index=['a', 'b', 'c', 'd'], dtype=float)
# print(data2)
# print(data2["a"])
#
# x = np.arange(5)
# data = pd.Series(x)
# print(data)
#
# population_dict = {"Beijing": 2145,
#                    "Shanghai": 2424,
#                    "Shenzhen": 1303,
#                    "Hangzhou": 981}
# population = pd.Series(population_dict)
# print(population)
#
# data = pd.Series(5, index=[100, 200, 300])
# print(data)

# population_dict = {"Beijing": 2145,
#                    "Shanghai": 2424,
#                    "Shenzhen": 1303,
#                    "Hangzhou": 981}
# population = pd.Series(population_dict)
# # print(pd.dataFrame(population, columns=['population']))
# GDP_dict = {"Beijing": 30320,
#             "Shanghai": 32680,
#             "Shenzhen": 24222,
#             "Hangzhou": 13468}
# GDP = pd.Series(GDP_dict)
# data = pd.DataFrame({"population": population, "GDP": GDP, "country": "China"})
# # print(data)
# data["per_GDP"] = data["GDP"]/data["population"]
# print(data)

# data = [{"a": i, "b": i*i} for i in range(3)]
# print(data)
# print(pd.dataFrame(data))
#
# data = np.random.randint(10, size=(3, 2))
# print(data)
# print(pd.dataFrame(data, columns=["qwe", "eqw"], index=['a', 'b', 'c']))



"""性质"""
#属性
# print(data.values)
# print(data.index)
# print(data.columns)
# print(data.size)
# print(data.shape)
# print(data.dtypes)

#索引
# print(data.GDP)
# print("Beijing:")
# print(data.loc[["Beijing", "Hangzhou"]])
# print(data.iloc[0])
# print(data.iloc[[1, 3]])
# print(data.iloc[0, 1])

#切片
# datas = pd.date_range(start='2019-01-01', periods=6)
# df = pd.dataFrame(np.random.randn(6, 4), index=datas, columns=['A', 'B', 'C', 'D'])
# print(df)
# print(df.loc["2019-01-01":"2019-01-03"])
# print(df.iloc[0:3])
# print(df.loc[:, "A": "C"])
# print(df.iloc[:, 0: 3])
# print(df.loc["2019-01-02": "2019-01-03", "C": "D"])
# print(df.iloc[1: 3, 2:])
# print(df.loc["2019-01-04": "2019-01-06", ["A", "C"]])
# print(df.iloc[3:, [0, 2]])
# print(df > 0)
# print(df[df > 0])
# print(df.A > 0)
# df2 = df.copy()
# df2["E"] = ['one', 'one', 'two', 'three', 'four', 'three']
# print(df2)
# ind = df2["E"].isin(["two", "four"])
# print(ind)
# print(df2[ind])

# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('2019-01-01', periods=6))
# # print(s1)
# df["E"] = s1
# print(df)
# df.loc["2019-01-01", "A"] = 0
# print(df)
# df.iloc[0, 1] = 0
# print(df)
#
# #index and columns
# df.index = [i for i in range(len(df))]
# print(df)
# df.columns = [i for i in range(df.shape[1])]
# print(df)


"""数值运算"""
# datas = pd.date_range(start='2019-01-01', periods=6)
# df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=["A", "B", "C", "D"])
# print(df)
# print(df.head(3))
# print(df.tail(3))
# df.iloc[0, 3] = np.nan
# print(df)
# print(df.info())

# x = pd.DataFrame(np.arange(4).reshape(1, 4))
# print(x+5)
# print(np.exp(x))

# np.random.seed(42)
# x = pd.DataFrame(np.random.randint(10, size=(3, 3)), columns=list("ABC"))
# print(x)
# print(x.iloc[0])
# print(x/x.iloc[0])
# print(x.A)
# print(x.div(x.A, axis=0))
# print(x.div(x.iloc[0], axis=1))

# A = pd.DataFrame(np.random.randint(0, 20, size=(2, 2)), columns=list("AB"))
# print(A)
# B = pd.DataFrame(np.random.randint(0, 10, size=(3, 3)), columns=list("ABC"))
# print(B)
# print(A.add(B, fill_value=0))

# y = np.random.randint(3, size=20)
# print(y)
# print(np.unique(y))
# from collections import Counter
# print(Counter(y))
# y1 = pd.DataFrame(y, columns=["A"])
# print(y1)
# print(np.unique(y1))
# print(y1["A"].value_counts())

# print(data.sort_values(by="per_GDP", ascending=False))

# data = pd.DataFrame(np.random.randint(20, size=(3, 4)), index=[2, 1, 0], columns=list("CBAD"))
# print(data)
# print(data.sort_index(axis=0))
# print(data.sort_index(axis=1, ascending=False))

# df = pd.DataFrame(np.random.normal(2, 4, size=(6, 4)), columns=list("ABCD"))
# print(df)
# print(df.count())
# print(df.sum(axis=1))
# print(df.max(axis=0))
# print(df.idxmax())
# print(df.mean())
# print(df.var())
# print(df.std())
# print(df.describe())

# print(df.apply(lambda x: x.max()-x.min()))
# def my_describe(x):
#     return pd.Series([x.count(), x.mean(), x.max(), x.std()],
#                      index=["count", "mean", "max", "std"])
# print(df.apply(my_describe))

# data = pd.DataFrame(np.array([[1, np.nan, 2],
#                              [np.nan, 3, 4],
#                              [5, None, 6],
#                               [7, 8, 9]]), columns=["A", "B", "C"])

# print(data.isnull())
# print(data.notnull())
# print(data.dropna())
# print(data.dropna(axis="columns"))
# data["D"] = np.nan
# print(data)
# print(data.dropna(axis="columns", how="any"))

# fill = data.mean()
# print(data.fillna(value=fill))
# print(data)


"""合并"""
# def make_df(cols, ind):
#     data = {c: [str(c)+str(i) for i in ind] for c in cols}
#     return pd.DataFrame(data, ind)

# df_1 = make_df("AB", [1, 2])
# df_2 = make_df("AB", [3, 4])
# print(df_1)
# print(df_2)
# print(pd.concat([df_1, df_2]))

# df_3 = make_df("AB", [0, 1])
# df_4 = make_df("CD", [0, 1])
# print(df_3)
# print(df_4)
# print(pd.concat([df_3, df_4], axis=1))

# df_5 = make_df("AB", [1, 2])
# df_6 = make_df("AB", [1, 2])
# print(df_5)
# print(df_6)
# print(pd.concat([df_5, df_6], axis=1, ignore_index=True))

# df_9 = make_df("AB", [1, 2])
# df_10 = make_df("BC", [1, 2])
# print(df_9)
# print(df_10)
# print(pd.merge(df_9, df_10))

# population_dict = {"city": ("Beijing", "Hangzhou", "Shenzhen"),
#                   "pop": (2134, 3453, 1321)}
# population = pd.DataFrame(population_dict)
# print(population)
# GDP_dict = {"city": ("Beijing", "Shanghai", "Hangzhou"),
#             "GDP": (3423, 3534, 3421)}
# GDP = pd.DataFrame(GDP_dict)
# print(GDP)
#
# city_info = pd.merge(population, GDP, how="outer")
# print(city_info)


"""分组"""
df = pd.DataFrame({"key": ['A', 'B', 'C', 'C', 'B', 'A'],
                   "data1": range(6),
                   "data2": np.random.randint(0, 10, size=6)})
# print(df)
# print(df.groupby("key").sum())
# print(df.groupby("key").mean())
# print(df.groupby("key")["data2"].sum())
# for data, group in df.groupby("key"):
#     print("{0:5} shape={1}".format(data, group.shape))
# print(df.groupby("key")["data1"].describe())
# print(df.groupby("key").aggregate(["min", "median", "max"]))

#过滤
# def filter_func(x):
#     return x["data2"].std() > 4
# print(df.groupby("key")["data2"].std())
# print(df.groupby("key").filter(filter_func))

#转换
print(df.groupby("key").transform(lambda x: x-x.mean()))

#分组键
# L = [0, 1, 0, 1, 2, 0]
# print(df.groupby(L).sum())

#用字典索引映射到分组
df2 = df.set_index("key")
print(df2)
mapping = {"A": "first", "B": "constant", "C": "constant"}
print(df2.groupby(mapping).sum())


















