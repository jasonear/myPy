from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello Worl ~```````````````哈哈哈哈！'

if __name__ == '__main__':
   app.run()