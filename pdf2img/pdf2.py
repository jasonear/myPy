import os
from PyPDF2 import PdfFileReader
from PIL import Image

def pdf_to_img(pdf_path, output_folder, page_no=0):
    # 打开PDF文件
    pdf = PdfFileReader(pdf_path)
    # 获取第一页（也可以获取其他页，只需改变page_no的值）
    page = pdf.getPage(page_no)
    text = page.extractText()  # 提取文本
    # 将文本转换为图片（这里只是一个示例，实际上文本不能转换为图片）
    text_img = Image.frombytes('RGBA', (100, 200), text.encode('utf-8'), 'raw')
    text_img.save(os.path.join(output_folder, f'page_{page_num}_text.jpg'), 'JPEG')


# 调用函数，将PDF转换为图片
pdf_to_img('pdf2img\demo.pdf', 'output_folder')