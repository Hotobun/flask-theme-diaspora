from flask import url_for, render_template 
import sys 
sys.path.append(".")
from app.database import db 
from app.setting import config
from flask import Blueprint


index_bp = Blueprint("index",__name__ )
  
@index_bp.route("/")
def home(): 
    image = config.index_image
    if "http" not in image:
        image = url_for("static", filename = config.index_image)
    d = { 
    'welcome' : db.query_filename("welcome"),
    'more' : url_for('jsonapi.get_json', args = "{}{}{}".format('index',config.jsonurl_split,1)) ,
    'gov'     : config.gov, 
    'index_imageurl' : image ,
    'copyright' : config.copyright,
    }
    p_here = {
        'letter':23333,
        'view':11111,
        'like': 56668,
    }
    return render_template("index.html", **d, p_here = p_here ) 