import os

index_archive_count = 5 

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flaskcocoa'
USERNAME = 'root'
PASSWORD = 'pass'
# mysql数据库URI
# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

# 数据库文章字符数上限 
db_text_count = 100000

# 评论未填写用户名的默认名称
default_user_name = "未署名的热心网友"

# 文章默认图片 img目录不要有前斜杠
define_coverimg = 'img/cover.jpg'

# json请求api分隔字符  # json/tag+jsonurl_split+count --> url.split(jsonurl_split) --> [tag, count] 
jsonurl_split = "helloworld"

# 文章路径
archive_path = os.path.join(os.getcwd(), "_posts") 

# 创建数据库原生语句
# CREATE DATABASE flaskcocoa DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

 

"""
例: 原主题
    <meta name="keywords" content="素锦, inspiration, customization, rainmeter, design, web, 壁纸, 设计, 收集, wallpaper, collection, jaku, icon">
    <meta name="description" content="世界上每个角落都有人过着相似的人生">
    <meta name="author" content="LoeiFy">
""" 
description = '我喜欢短发妹子'
sitename = "馒++"
keywords = "flask, cocoa, 壁纸, 素锦,  音乐"
author = 'Hoto cocoa'

# nav_p 
# 例 '© 2020 素锦. Powered by WordPress. ' # 好像还没用 
nav_p = '© 2020 Hotobun. Powered by Flask. '


# copyright
copyright = '''
    <p id="copyright">
        &copy; 2020 Hotobun.
        Powered by <a href="https://dormousehole.readthedocs.io/en/latest/" title="Flask" target="_blank" rel="noopener">Flask</a>
        Theme <a href="https://github.com/LoeiFy/Diaspora" title="Diaspora" target="_blank" rel="noopener">Diaspora</a>
        by <a href="https://github.com/LoeiFy" title="LoeiFy" target="_blank" rel="noopener">LoeiFy</a>
        and <a href="https://github.com/Fechin/hexo-theme-diaspora" title="Fechin" target="_blank" rel="noopener">Fechin.</a> 
    </p>
'''




# gov 备案号
# 例 '湘ICP备14010307号'
gov = '备案是不可能备案的 这辈子都不可能备案的'

# 文章href前缀 不要有斜杠
article_prefix = "article"

# music 从static/music下面找的 直接写文件名
# 暂时没有每个文章分配不同音乐
music = 'gabriel.mp3'

# 图床首页 使用时 image_site + img/filename.jpg 大概
# 不使用图床的话 要用 url_for("static", filename='img/filename.jpg') 
image_site = "http://hotobun.gitee.io/hexo/"

index_image = 'img/index.jpg'
# index_image = 'https://s2.ax1x.com/2020/01/17/lxgfxO.jpg'
# index_image = "https://s2.ax1x.com/2020/01/17/lzICLV.jpg"
# index_image = "http://hotobun.gitee.io/hexo/img/index.png"


if __name__ == "__main__":
    print(archive_path)