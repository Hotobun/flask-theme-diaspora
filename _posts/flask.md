---
title: flask
date: 2019-12-04 23:35:38
tags:
- python
- flask 
categories: 网络 
cover: /img/flask.jpg
---

## 建立第一个项目
```
from flask import Flaskapp = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```
运行  hello.py  
$ python hello.py  
\* Running on http://127.0.0.1:5000  
route()装饰器告诉Flask什么样的URL能触发函数。  
用户访问 / 首页时调用hello_world()函数
app.run(host= None, port=None , debug=False, **options )  
* host : 主机ip地址 默认127.0.0.1，如果需要开放给其他机器访问可以填0.0.0.0  
* port : 端口 默认5000  
* debug: 调试模式  
* options: 官方没讲 只丢了个连接。    

***
## 变量规则    
* 在route装饰器括号内 可以使用特殊标记 <var_name>传递参数 例：  
```
@app.route('/user/<usrname>')
def show_name(username):
    # 函数参数username 必须与装饰器内特殊标记变量名一致
    return 'hello %s' % username

@app.route('/user/<int:number>'):
def show_number(number):
    return '这里接收了数字：%d' % number
    # 可以用这样的形式指定变量类型 <type:name>
    # 类型无法转换则不匹配
    # 转换器有下面几种
         int : 接收整数
       float ：接收浮点数
        path ：路径类型 接收斜杠
```

***
## URL/ 重定向行为：  
1 @app.route('/url_one/')   # URL路径后有斜杠   
* 可以匹配 :   http://127.0.0.1:5000/url_one
* 这两个URL都会重定向到这:   http://127.0.0.1:5000/url_one/  
* 
2 @app.route('/url_two')    # URL路径后没有斜杠
* 不可以匹配: http://127.0.0.1:5000/url_two
* 可以匹配：http://127.0.0.1:5000/url_two/

这个行文使得遗忘斜杠时 允许关联的URL接任工作 保证URL唯一性  
如果规则以斜杠结尾 当用户不带斜杠的形式请求 用户被自动重定向到带有斜杠的也页面  
如果规则没有斜杠结尾 用户必须带斜杠请求 否则抛出404  

*** 
## URL路由规则
1 使用 flask.Flask.route() 装饰器  
2 使用 flask.Flask.add_url_rule() 函数  
3 直接访问暴露为 flask.Flask.url_map 的底层的Werkzeug 路由系统  ？？啥东西  

***
## 上传文件
用 Flask 处理文件上传很简单。只要确保你没忘记在 HTML 表单中设置enctype="multipart/form-data" 属性，不然你的浏览器根本不会发送文件。已上传的文件存储在内存或是文件系统中一个临时的位置。你可以通过请求对象的 files属性访问它们。每个上传的文件都会存储在这个字典里。它表现近乎为一个标准的 Python file 对象，但它还有一个 save() 方法，这个方法允许你把文件保存到服务器的文件系统上。这里是一个用它保存文件的例子:  
```
from flask import request

@app.route('/upload', methods=['GET', 'POST'])def upload_file():
if request.method == 'POST':
    f = request.files['the_file'] #　这个the_file 与模版里上传文件名一致
    f.save('/path/file_name')
```

传文件可是个经典的好问题了。文件上传的基本概念实际上非常简单， 他基本是这样工作的:    
1 一个\<form> 标签被标记有 enctype=multipart/form-data ，并且在里面包含一个\<input type=file> 标签。  
2 服务端应用通过请求对象上的 files 字典访问文件。  
3 使用文件的 save() 方法将文件永久地保存在文件系统上的某处。  

```
import os
from flask
import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
```
UPLOAD_FOLDER 是我们储存上传的文件的地方，而ALLOWED_EXTENSIONS 则是允许的文件类型的集合。然后我们手动为应用添加一个的 URL 规则。我们通常很少这样做，但是为什么这里要如此呢？原因是我们希望实际部署的服务器 (或者我们的开发服务器）来为我们提供这些文件的访问服务，所以我们只需要一个规则用来生成指向这些文件的 URL 。  
```
def allowed_file(filename):
    # 这里检查后缀名
   return '.' in filename and \
       filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
       file = request.files['file']
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           return redirect(url_for('uploaded_file',filename=filename))
   return '''
       <!doctype html>
       <title>Upload new File</title>
       <h1>Upload new File</h1>
       <form action="" method=post enctype=multipart/form-data>
         <p><input type=file name=file>
           <input type=submit value=Upload>
         </form> 
```

尽量使用secure_filename() 作为文件名  
现在我们来研究一下这个函数的功能:  
`>>> secure_filename('../../../../home/username/.bashrc')`  
`'home_username_.bashrc'`  

指定一个文件大小的上限
```
from flask import Flask, Request

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制了16M 超出会抛 RequestEntityToolarge异常
```

![flask1](/img/archive_img/flask1.png)
![flask2](/img/archive_img/flask2.png)

***
##  静态文件  
render_template 和 url_for 的应用:  
![flask3](/img/archive_img/flask3.png)
![flask4](/img/archive_img/flask4.png)

html模版语言中  
```
    {{ value_name }}  两个花括号内的是变量名 值是从render_template参数传过去  
    {% if .. %}    花括号类似编程语法 注意结束时 endif    
    {% endif %}    for 等操作同理  
```


***
##  模版渲染  
render_template 渲染模版 默认传进的参数 带有html标签符会自动转义  
如果想要从render_template传递带有标签符的内容 使用Markup函数：  
\# 只有 Markup 不转义  
![flask5](/img/archive_img/flask5.png)
![flask6](/img/archive_img/flask6.png)

***
##  用户注册
![flask7](/img/archive_img/flask7.png)  
request.form 接收用户post的表单 用法与字典类似。  
request.args 接收用户get的url参数  

*** 
##  配置文件  
* 在项目目录下 新建一个config.py 文件  
* 在文件里面写入配置信息  
* 项目主文件通过以下方式即可导入  
```
import config  
app.config.from_object(config)
```

***
## 连接数据库
使用mysql 依赖库： pymysql、 flask_sqlalchemy  
* 创建 config.py
* 写入 SQLALCHEMY_DATABASE_URI
![flask8](/img/archive_img/flask8.png)
![flask9](/img/archive_img/flask9.png)

***
## ORM模型
模型类需要继承 上面第7行的db.Model属性  
需要映射到表中的属性，必须写成 db.Column()的数据类型  
* db.Integer：整形  
* db.String： 字符串，需要指定最长的长度  
* db.Text：  text类型  
* primary_key  --> 主键  
* autoincrement --> 自增长  
* nullable    --> 默认可为空  False则不允许为空  

最后调用 db.create_all() 将模型创建到数据库
![flask10](/img/archive_img/flask10.png)

*** 
## 数据库增删改查
定义若干视图函数，当url访问时再调用函数
```
@app.route("/")
def sql_xxx():
    # 增:
    article1 = Article(title = 'aaaaa', content = 'bbbbb')
    db.session.add(article1)  # 通过session属性 增加到数据库事务
    db.session.commit()       # 这句话才是将事务提交 将数据保存至数据库
   
    ---------分割线
    # 查：
       # Article继承自db.Model，通过父类query属性进行查找操作 所有查找必须通过这个属性
       # 通过filter过滤 参数: 模型类.属性名 = val  
       # .all()后下标可以换成.first() 如果没有数据 返回None  都是取出第一个数据
    article2 = Article.query.filter(Article.title=='aaaaa').all()[0]
    print ("title   --> ", article2.title)
    print ('content --> ', article2.content)

   ---------分割线
    # 改:
    1 把数据查找出来
    2 修改这条数据
    3 提交事务
    article3 = Article.query.filter(Article.title == 'aaaaa').first()
    article3.content = 'new content'
    db.session.commit()

   ---------分割线
    # 删:
    1 把数据查找出来
    2 把这条数据删除
    3 做事务提交
    article4 Article.query.filter(Article.title == 'aaaaa').first()
    db.session.delete(article4)
    db.session.commit()
```

***
## flask_script 使用命令行操作Flask:
![flask11](/img/archive_img/flask11.png)  
![flask12](/img/archive_img/flask12.png)  
![flask13](/img/archive_img/flask13.png)  
![flask14](/img/archive_img/flask14.png)  

***
## 循环引用问题：
主文件导入Models    
Models文件又导入主文件的app 就会产生循环引用的问题  
解决方法：  
新建一个exts.py 里面创建SQLAlichemy实例
```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```
Models和主文件都从这里导入db 就切断循环引用  
主文件内使用  
```
from exts import db
db.init_app(app)
```
