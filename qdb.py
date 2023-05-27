import os
import pymssql

server = "192.168.0.57"  # 服务器IP或服务器名称
user = "sa"  # 登陆数据库所用账号
password = "sa"  # 该账号密码

conn = pymssql.connect(server, user, password, database='test')
cursor = conn.cursor()

cursor.execute("select top 10 * from address2point_temp1")  # 向数据库发送SQL命令
myrow = cursor.fetchone()
while myrow:
    print(myrow[2]+',' + myrow[4])
    myrow = cursor.fetchone()

conn.close()

# 写入数据
# cursor.execute("insert into dbo.test ([NO.],Name,Address) values ('003','张三','郑州') ")
# conn.commit()
# conn.close()
