from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    # 返回一条消息，表示服务创建成功
    return{'message':'你已经正确创建 FastApi 服务！ waaakkkkkk'}


@app.get('/query/{uid}')
def query(uid):
    # 返回一条消息，表示查询的 uid
    msg=f'你查询的 uid 为：{uid}'
    return {'success':True,'msg':msg}