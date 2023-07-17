from pywebio.input import *
from pywebio.output import *
from pywebio import STATIC_PATH
from functools import partial

# 输入

# # Password input
# password = input("Input password", type=PASSWORD)
# put_text('password = %r' % password)

# # Drop-down selection
# gift = select('Which gift you want?', ['keyboard', 'ipad'])
# put_text('gift = %r' % gift)


# # File Upload
# img = file_upload("Select a image:", accept="image/*")
# if img:
#     put_image(img['content'], title=img['filename'])


# mytext = input('This is label', type=TEXT, placeholder='This is placeholder',
#         help_text='This is help text', required=True)
# put_text('thisTEXT = %r' % mytext)



# def check_age(p):  # return None when the check passes, otherwise return the error message
#     if p < 10:
#         return 'Too young!!'
#     if p > 60:
#         return 'Too old!!'

# age = input("How old are you?", type=NUMBER, validate=check_age)
# put_text('age = %r' % age)


# def check_form(data):  # return (input name, error msg) when validation fail
#     if len(data['name']) > 6:
#         return ('name', 'Name too long!')
#     if data['age'] <= 0:
#         return ('age', 'Age can not be negative!')

# data = input_group("Basic info",[
#   input('Input your name', name='name'),
#   input('Input your age', name='age', type=NUMBER)
# ], validate=check_form)
# put_text(data['name'], data['age'])



# 输出

# # Text Output
# put_text("Hello world!")

# # Table Output
# put_table([
#     ['Commodity', 'Price'],
#     ['Apple', '5.5'],
#     ['Banana', '7'],
# ])

# # Image Output

put_image(open(STATIC_PATH +'/image/apple-touch-icon.png', 'rb').read())  # local image
put_image('https://www.wpdi.cn/files/upload/20170813/about-us-2.jpg')  # internet image

# # Markdown Output
# put_markdown('~~Strikethrough~~')

# # File Output
# put_file('hello_word.txt', b'hello word!')

# # Show a PopUp
# popup('popup title', 'popup text content')

# # Show a notification message
# toast('New message 🔔')


# put_table([
#     ['Type', 'Content'],
#     ['html', put_html('X<sup>2</sup>')],
#     ['text', '<hr/>'],  # equal to ['text', put_text('<hr/>')]
#     ['buttons', put_buttons(['A', 'B'], onclick=put_text)],
#     ['image111111',put_image('https://www.wpdi.cn/files/upload/20170813/about-us-2.jpg') ],
#     ['markdown', put_markdown('`Awesome PyWebIO!`')],
#     ['file', put_file('hello.text', b'hello world')],
#     ['table', put_table([['A', 'B'], ['C', 'D']])]
# ])


# popup('Popup title', [
#     put_html('<h3>Popup Content</h3>'),
#     'plain html: <br/>',  # Equivalent to: put_text('plain html: <br/>')
#     put_image('https://www.wpdi.cn/files/upload/20170813/about-us-2.jpg'),
#     put_table([['A', 'B'], ['C', 'D']]),
#     put_button('close_popup()', onclick=close_popup)
# ])


# def edit_row(choice, row):
#     put_text("You click %s button ar row %s" % (choice, row))

# put_table([
#     ['Idx', 'Actions'],
#     [1, put_buttons(['edit', 'delete'], onclick=partial(edit_row, row=1))],
#     [2, put_buttons(['edit', 'delete'], onclick=partial(edit_row, row=2))],
#     [3, put_buttons(['edit', 'delete'], onclick=partial(edit_row, row=3))],
# ])