import sys, json
sys.path.append(".") 
from app.setting import config
from app.database import db
from flask import render_template, url_for, Response 
from flask import Blueprint

json_bp = Blueprint("jsonapi",__name__, url_prefix="/json")  

@json_bp.route("/<args>")
def get_json(args):
    if config.jsonurl_split in args:
        tag, index = args.split(config.jsonurl_split)
    else:
        return {}
    sql_data = db.query_archive(tag, index)
    temp = []
    number = int(index) - 1
    for item in sql_data:  
        temp.append( { 
            "filename" : item.filename,
            "href":item.href,
            # "imgurl": url_for('static', filename=item.imgurl) ,
            "imgurl": "http://hotobun.gitee.io/hexo/"+item.imgurl,
            # "imgurl" : url_for("static", filename = "img/number/{}.jpg".format(number%8 + 1 )),
            "date":  item.date.strftime("%B %d,%Y"),
            "abstract": item.abstract,
            "title": item.title,
            }
        )
        number += 1
    if len(temp) <= config.index_archive_count:
        more = "end"
    else:
        more = url_for('jsonapi.get_json', args = "{}{}{}".format('index',config.jsonurl_split,int(index)+config.index_archive_count))
    data = {
        "data": temp[:config.index_archive_count],
        "more": more,
    } 
    return Response(json.dumps(data), mimetype="application/json")


if __name__ == "__main__":
    print("hello world")

    