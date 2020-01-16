from flask import url_for, render_template 
import sys 
sys.path.append(".")
from app.database import db 
from app.setting import config
from flask import Blueprint


index_bp = Blueprint("index",__name__ )
  
@index_bp.route("/")
def home(): 
    d = { 
    'welcome' : db.query_filename("welcome"),
    'more' : url_for('jsonapi.get_json', args = "{}{}{}".format('index',config.jsonurl_split,1)) ,
    'gov'     : config.gov, 
    'index_imageurl' :  config.index_image,
    'copyright' : config.copyright,
    }
    return render_template("index.html", **d ) 