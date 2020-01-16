from flask import url_for, render_template, request, redirect
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


comment_bp = Blueprint("comment",__name__, url_prefix="/comment")

@comment_bp.route("/<filename>", methods = ['GET','POST'])
def comment_post(filename):
    if request.method == "POST":
        data = request.form.to_dict()
        low = db.query_comment(fid='invest', limit=1 )[0]
        if low.comment == data['comment']:  
            if low.root == int(data['root']): 
                c = datetime.datetime.now() - low.date 
                if c.seconds < 10:
                    return redirect(url_for("article.archive",filename=data['fid'])  )
        g = Gravatar(data['email'])
        r = requests.get(g.get_image(default="404"))
        if r.status_code != 404:
            data['vcardurl'] = g.get_image(default="http://hotobun.gitee.io/hexo/img/number/8.jpg")
        db.insert_comment(data)

    return redirect(url_for("article.archive",filename=data['fid'])  )



def get_sql_comments(filename):
    # rtype : list
    data = db.query_comment(filename)
    # print("查询到{}条数据".format(len(data)))
    root0 = []
    children = []
    for i in data:
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
    get_sql_comments('invest')