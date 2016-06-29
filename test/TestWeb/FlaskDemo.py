from flask.app import Flask
from flask.globals import request

app=Flask(__name__)

#访问根目录是响应home函数
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['GET','POST'])
def signin_form():
    return r'''<form action="/solvesign" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
@app.route('/solvesign',methods=['POST'])
def sigin():
    #从request对象中读取表单内容：
    if request.form['username']=='admain' and request.form['password']=='123456':
        return r'<h3>Hello Bob!</h3>'
#使服务器运行
app.run()