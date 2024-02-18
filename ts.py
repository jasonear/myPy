import requests
# 请求 https://www.codegeex.cn/ 网站，获取返回响应状态、响应头、响应内容，并输出

# 向指定URL发送GET请求，获取响应
response = requests.get('https://www.codegeex.cn/')

# 打印响应状态码
print('响应状态：', response.status_code)
# 打印响应头
print('响应头：', response.headers)
# 打印响应内容
# print('响应内容：', response.text)