from sqlalchemy import Column,Integer,String, DateTime, func, Boolean, Text 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
import sys 
sys.path.append(".")
from app.setting import config
import datetime, random

engine = create_engine(config.DB_URI,echo=False)
Session = sessionmaker(bind=engine)
session = Session()
# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)


class Archive(Base):
    # 定义表名
    __tablename__ = 'archive'

    # 将id设置为主键，并且默认是自增长的
    # Column常用参数:
    # default：默认值。
    # nullable：是否可空。
    # primary_key：是否为主键。
    # unique：是否唯一。
    # autoincrement：是否自动增长。
    # onupdate：更新的时候执行的函数。
    # name：该属性在数据库中的字段映射。
    filename = Column(String(100),primary_key = True, unique=True)
    href = Column(String(100))
    imgurl = Column(String(100))
    date = Column(DateTime, name = "time")
    title = Column(String(40))
    abstract = Column(String(81))
    text = Column(Text(config.db_text_count))
    tags = Column(String(100))
    isdel = Column(Boolean, default = True)

    __mapper_args__ = {
        "order_by": date.desc()
    }
    
    def __repr__(self):
        return '<Archive( title="{} ")>'.format( self.title)


    def update_archives(self, filenames):
        archives = session.query(Archive).all()
        for i in archives:
            if i.filename not in filenames:
                i.isdel = True 

    def insert(self, item):
        # item type : dict
        # 插入数据 
        if type(item) == dict:       
            temp = session.query(Archive).filter( item.get("filename") == Archive.filename ).all()
            if temp and type(temp[0]) == Archive: 
                new = temp[0] 
            else:
                new = Archive()

            new.filename = item.get("filename")
            new.href = "/{}/{}".format(config.article_prefix, item.get("filename"))
            new.imgurl = item.get('cover').strip("/") if len(item.get("cover")) > 5 else config.define_coverimg
            new.date = item.get('date', '2009-10-16 15:35:38') 
            new.title = item["title"]
            new.abstract = item["abstract"][:80]
            new.tags = item["tags"] 
            new.text = item['text']
            new.isdel = False

            session.add(new)  
            session.commit()        

    def query_archive(self, tag, index):
        # tag type : str
        # index type : int
        '''
        tag选择查询的标签
        index 控制查询几条语句 该值设置在 config.py 文件中 index_archive_count
        offset 控制偏移量 
        例：
            mysql> select * from archive
                    where tags likek "%tag%"
                    limit offset index
                    ;
        '''
        if tag == 'index':
            tag = ''
        target = session.query(Archive).filter( Archive.isdel == False, Archive.tags.like("%{}%".format(tag))).limit(config.index_archive_count+1).offset( index ).all()
        return target 

    def query_filename(self, filename):
        target = session.query(Archive).filter(Archive.filename == filename).all()
        if len(target) > 0 and type(target[0]) == Archive:
            return target[0]
        else:
            return False

    def drop(self,):
        Archive.__table__.drop(engine)
        print("drop ",Archive.__tablename__)

class Tags(Base):
    # 定义表名
    __tablename__ = 'tags'

    # 将id设置为主键，并且默认是自增长的
    # Column常用参数:
    # default：默认值。
    # nullable：是否可空。
    # primary_key：是否为主键。
    # unique：是否唯一。
    # autoincrement：是否自动增长。
    # onupdate：更新的时候执行的函数。
    # name：该属性在数据库中的字段映射。
    tag = Column(String(100),primary_key = True, unique=True) 
    
    def __repr__(self):
        return '<tags ( tag="{} ")>'.format( self.tag)

    def update(self, items):
        for i in items:
            new = Tags()
            new.tag = i
        
    def drop_tag(self):
        self.drop()
        
class Comment(Base):
    # 定义表名
    __tablename__ = 'comment'

    # 将id设置为主键，并且默认是自增长的
    # Column常用参数:
    # default：默认值。
    # nullable：是否可空。
    # primary_key：是否为主键。
    # unique：是否唯一。
    # autoincrement：是否自动增长。
    # onupdate：更新的时候执行的函数。
    # name：该属性在数据库中的字段映射。 
    id = Column(Integer,primary_key = True, unique=True)
    date = Column(DateTime, default=datetime.datetime.now, )
    root = Column(Integer)
    fid = Column(String(100))
    author = Column(String(100))
    vcardurl = Column(String(300))
    comment = Column(String(1000))
    site = Column(String(300))
    email = Column(String(300))
    ip = Column(String(300))
    isdel = Column(Boolean, default = False )

    __mapper_args__ = {
        "order_by": date.desc()
    }
    
    def __repr__(self):
        return '<Comment( {}:{} )>'.format( self.author, self.comment[:20])

    def insert(self, item):
        # item tyep: dict
        if type(item) == dict:       
            new = Comment()
            if item.get('id', False):
                new.id = item['id']
            new.root = item['root']
            new.fid = item['fid']
            if item.get('date', False):
                new.date = item['date']
            if not item['author']:
                new.author = config.default_user_name
            else:
                new.author = item['author']
            new.vcardurl = item.get('vcardurl', 'default_img')
            new.comment = item['comment']
            new.site = item['site']
            new.email = item['email']
            new.ip = item.get("ip", '')
            new.isdel = False

            session.add(new)
            session.commit()
            print("插入成功 ")

    def query(self, fid, limit = 0):
        if limit:
            target = session.query(Comment).filter( Comment.isdel == False, Comment.fid == fid ).limit(limit).all()
        else:
            target = session.query(Comment).filter( Comment.isdel == False, Comment.fid == fid ).all()
        return target

    def query_email(self, email):
        return session.query(Comment).filter( Comment.email == email ).all()
    
    def drop(self):
        Comment.__table__.drop(engine)
        print("drop ", Comment.__tablename__)

def Create_table():
    # 创建数据表
    Base.metadata.create_all()
    print("table {} 创建成功".format(Tags.__tablename__))
    print("table {} 创建成功".format(Archive.__tablename__))

if __name__ == "__main__":
    # print("uri -->", DB_URI)
    # # exit()
    # drop_archive()
    # update()
    Create_table()
 
 