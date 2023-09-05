from pdf2image import convert_from_path

# 指定要转换的PDF文件路径
pdf_file = "pdf2img\demo.pdf"  # 将文件路径替换为您的PDF文件路径

# 使用pdf2image库将PDF页面转换为JPG图像
images = convert_from_path(pdf_file)

# 保存JPG图像
for i, image in enumerate(images):
    jpg_filename = f"page_{i + 1}.jpg"  # 图像文件名，可以根据需要自定义
    image.save('data/'+jpg_filename, "JPEG")


# for i, image in enumerate(images):
#     jpg_filename = f"page_{i + 1}.png"
#     image.save('data/'+jpg_filename, "PNG")


print("PDF页面转换为图像完成！")