from flask import Flask
import sys 
sys.path.append(".")
from app.blog.jsonapi import json_bp
from app.blog.index import index_bp
from app.blog.article import article_bp
from app.blog.comments import comment_bp


def create_app():
    app = Flask(__name__, static_url_path='')

    app.register_blueprint(json_bp)
    app.register_blueprint(index_bp) 
    app.register_blueprint(article_bp)
    app.register_blueprint(comment_bp)
     
    return app

if __name__ == "__main__":
    print("hello world")

    