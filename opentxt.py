import os

# 读取文件内容
with open(r'./data/mytxt.csv', encoding='utf-8') as f:
    # content_list = f.readlines()
    # print(content_list)
    content = f.read()
    print(content)

print('------------------')


# 在文件结尾写入内容
with open(r'./data/mytxt1.txt', 'a', encoding='utf-8') as f:
    f.write('\n哈哈哈哈，写入文字！')
    f.writelines(['\n第一行', '\n第二行', '\n第三行'])
    print('{0}文件写入完毕！'.format('mytxt1.txt'))
