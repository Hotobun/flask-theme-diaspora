from flask import url_for, render_template 
import sys 
sys.path.append(".")
from app.database import db 
from app.setting import config
from flask import Blueprint
import markdown
import os
import mistletoe
from app.blog.comments import get_sql_comments


article_bp = Blueprint("article",__name__, url_prefix="/article")

@article_bp.route("/<filename>")
def archive(filename): 
    sql_item = db.query_filename(filename)
    if sql_item and sql_item.isdel == False:
        target_path = os.path.join(config.archive_path, filename + ".md")
        if os.path.isfile(target_path):
            d = {
                'sitename'      : config.sitename,
                'author'        : config.author,
                'keywords'      : config.keywords,
                'filename'      : sql_item.filename,
                'article_main'  : sql_item.text,
                'title'         : sql_item.title,
                'date'          : sql_item.date.strftime("%B %d,%Y"),
                'tags'          : sql_item.tags.split(" "),
                'active_music'  : url_for('static', filename = "music/{}".format(config.music)), 
                'form_post_url': url_for('comment.comment_post',filename = sql_item.filename)
            }
            # comments = get_sql_comments(sql_item.filename)
            comments = get_sql_comments(sql_item.filename)
            # print("d[article_content]", d['article_content']) 
            return render_template('article.html', **d, comments = comments)
    
    return "文章不存在"
 