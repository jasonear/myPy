from openpyxl import Workbook
 
 
def main():
    sheet_name = "表名1"
    row_count = 6  # 行数
    info_result = []
    page = 1
    while page <= row_count:
        info = ['a', 'b', 'c']  # 每行的内容
        info_result.append(info)
        page += 1
    # 写入Excel表格
    wb = Workbook()
    ws1 = wb.active
    ws1.title = sheet_name  # sheet名称
    for row in info_result:
        ws1.append(row)
    wb.save('拉钩职位信息.xls')  # Excel文件名称，保存文件
 
 
if __name__ == '__main__':
    main()