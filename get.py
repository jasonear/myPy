import json

# GET请求API接口,并对结果进行JSON解析
def getApi(host: str, url: str):
    """
    GET请求API接口,并对结果进行JSON解析
    :param host: 主机
    :param url: 地址
    :return: 对象
    """
    con = http.client.HTTPConnection(host)
    con.request('GET', url)
    response = con.getresponse()
    utf8 = response.read().decode('utf-8')
    decoded = json.loads(utf8)
    return decoded
