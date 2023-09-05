import pandas as pd
import time

# df = pd.read_excel('wrfile\mydata_m.xlsx')
# print('开始读取内容...')
# print(df)


# 读取excel的某一个sheet
df = pd.read_excel('wrfile\mydata_m.xlsx',sheet_name='Sheet1')
# print(df)

# 获取列标题
# print(df.columns)
print(df.loc[0].values[0:-1])

#获取列行标题
# print(df.index)

#制定打印某一列
# print(df['企业名称'])

#描述数据
# print(df.describe())


# t1 = time.time()
# for indexs in df.index:
#     print(df.loc[indexs].values[0:-1])
# t2=time.time()
# print("遍历数据耗时：%.2f 秒"%(t2-t1))

