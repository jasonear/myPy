# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from urllib.parse import quote

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Uselogs(Base):
    # 表的名字:
    __tablename__ = 'uselogs'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    userid = Column(String(20))
    mapid=Column(String(20))
    action=Column(String(100))
    dtime=Column(DateTime())

# 初始化数据库连接:
engine = create_engine('mssql+pyodbc://sa:'+'%s@'%quote('wpdi@2017') + '192.168.0.176:1433/GisData?driver=ODBC Driver 17 for SQL Server')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
mylog = session.query(Uselogs).filter(Uselogs.userid=='134').all()
# 打印类型和对象的name属性:
print('type:', type(mylog))
print(mylog[-1].action)
# 关闭Session:
session.close()