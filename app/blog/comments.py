from flask import url_for, render_template, request, redirect, make_response, Response
import sys 
sys.path.append(".")
from app.database import db 
from app.setting import config
from flask import Blueprint
import markdown
import os
import mistletoe
import datetime
from libgravatar import Gravatar
import requests
import random


comment_bp = Blueprint("comment",__name__, url_prefix="/comment")

def get_gravatar_image(email):
    '''
        输入email 判断这个邮箱是否有头像 
        有就保存 没有就返回 默认头像
    '''
    # 判断数据库有没有这个邮箱 有就直接用
    emails = db.query_comment_email(email)
    if len(emails) > 0:
        if emails[-1].vcardurl != 'default_img': 
            return emails[-1].vcardurl
    
    imgpath = os.path.join(config.cwd, 'app','static','img','gravatar') 
    g = Gravatar(email)
    r = requests.get(g.get_image(default="404"))

    if r.status_code == 404: 
        return "default_img"
    else: 
        i_type = r.headers.get('Content-Type','')[-3:].lower()
        if i_type not in ['jpg','png']:
            i_type = 'jpg'
        count = len(os.listdir(imgpath))
        filename = ''
        while filename == '':
            count += 1 
            imgname = '{}.{}'.format( count, i_type ) 
            target_filename = os.path.join(imgpath,  imgname )
            if os.path.isfile(target_filename):
                continue
            else:
                filename = target_filename
                break
        with open(filename, 'wb') as f:
            f.write(r.content)
        result = url_for('static', filename='img/gravatar/{}'.format(imgname))
        return result

@comment_bp.route("/<filename>", methods = ['GET','POST'])
def comment_post(filename):
    if request.method == "POST":
        data = request.form.to_dict()
        low = db.query_comment(fid='invest', limit=1 )
        if len(low) > 0:
            low = low[0]
            if low.comment == data['comment']:  
                if low.root == int(data['root']): 
                    c = datetime.datetime.now() - low.date 
                    if c.seconds < 10:
                        return redirect(url_for("article.archive",filename=data['fid'])  )

        if not data['author']:
            data['author'] = config.default_user_name
        data['vcardurl'] = get_gravatar_image(data['email']) 
        # data['comment'] = mistletoe.markdown(data['comment'])
        comment_text = '' 
        for i in data['comment'].split("\n"):
            if i.replace("\r", '').replace(" ",'').replace("\t",''):
                comment_text += "<p>{}</p>".format(i.replace("\r", ''))  
 
        data['comment'] = comment_text
        data['ip'] = request.remote_addr 
        db.insert_comment(data) 
    resp = make_response(redirect(url_for("article.archive",filename=data['fid'])))
    resp.set_cookie('user',data['author'], max_age=config.cookie_max_age)
    resp.set_cookie('email',data['email'], max_age=config.cookie_max_age)
    resp.set_cookie('site',data['site'], max_age=config.cookie_max_age)
    return resp

def get_sql_comments(filename):
    # rtype : list
    data = db.query_comment(filename)
    # print("查询到{}条数据".format(len(data)))
    root0 = []
    children = []
    for i in data:
        if i.vcardurl == 'default_img':
            i.vcardurl = url_for("static",filename='img/number/{}.jpg'.format(random.randint(1,8)))
        if i.root == 0:
            i.add_comms = []
            root0.append(i)
        else:
            children.append(i) 
    queue = []
    b = children.copy()
    for r in root0:
        for c in children:
            if c.root == r.id: 
                if root0.index(r) not in queue:
                    queue.append(root0.index(r))  
                b.remove(c)
                r.add_comms.append(c)
                r.add_comms.sort(key= lambda i : i.date )
    root0.sort(key= lambda i : i.date , reverse=True )
 
    for i in b:
        for j in queue:
            for k in root0[j].add_comms:
                if k.id == i.root:
                    root0[j].add_comms.insert(root0[j].add_comms.index(k)+1, i)
     
    return root0



if __name__ == "__main__":
    # get_sql_comments('invest')
    get_gravatar_image('349924492@qq.com')