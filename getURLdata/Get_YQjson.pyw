import requests
import os
import time
import schedule

desktop_path = "D:\\00_jason\\0_data\\"  # 新创建的txt文件的存放路径

def text_create(desktop_path,name, msg):
    full_path = desktop_path + name + '.json'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w',encoding='utf-8')
    file.write(msg) 
    file.close()


def job(req_url,f_name):
    r=requests.get('https://{0}'.format(req_url))
    filename = f_name +'_'+ time.strftime('%Y-%m-%d_%H%M%S')
    print('{1} r.status_code: {0}'.format(r.status_code,filename))
    text_create(desktop_path, filename, r.text)
    print('OK')


def dojob():
    job('ncov-cdn.sndo.com/getNcov.djson','getNcov')
    #job('ncov-cdn.sndo.com/quarantine/getQuarantineAll.djson','getQuarantineAll')


schedule.every(5).seconds.do(dojob) # 每10秒执行一次

while True:
    schedule.run_pending()
    time.sleep(1)




 

