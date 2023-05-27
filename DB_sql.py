from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
postgres_conn_url = 'postgresql://'+self.postgres_username+':%s@'%quote('密码')+ self.postgres_host +'/'+self.postgres_db_name
pg_engine = create_engine(self.postgres_conn_url)

#方式1：pyodbc需要安装ODBC Driver 17 for SQL Server
sqlserver_conn_url = 'mssql+pyodbc://'+self.sqlserver_username+':%s@'%quote(self.sqlserver_password)+ self.sqlserver_host +'/'+self.sqlserver_db_name+"?driver=ODBC Driver 17 for SQL Server"
sqlserver_engine = create_engine(sqlserver_conn_url)

glgc_ztzb_sql = text(f"select ljkd,ljjj,zbz from tuguisuo_ldss.glgc_ztzb where gldj='{gldj.value}' and cdsl='{cdsl.value}' and dxlb='{dxlb.value}';")
with Session(postgre_engine) as session:
    glgc_ztzb_results = session.execute(glgc_ztzb_sql).all()