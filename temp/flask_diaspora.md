---
title: Flask博客Diaspora主题
date: 2020-1-11 15:01:55
tags: 
- python
- flask
categories:
cover: img/flask_diaspora.jpg
---

花了几天写移植主题  
已使用flask做后台  

坑太多 慢慢填   
hexo已部署到码云 同步更新

*** 
## flask-theme-diaspora

参数都在`app/setting/config.py`填写

文章放在_posts

需要两个logo图标
* `app/static/img/site/logo.png` 首页左上角logo 背景透明
* `app/static/img/site/logo_min.png` 浏览器最上方标题旁边的图标 

*** 
数据库 
* 进入mysql创建数据库 
  * `CREATE DATABASE flaskcocoa DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;`
* `python app/database/archive.py` 创建数据库并写入文章数据
* `python main.py` 运行



## 坑
* markdown渲染引擎 代码块还没有高亮 待填
```
    python自带的不友好 最后选择了 mistletoe
    注意表单格式 要格式化文档 不对齐竖线 | 的会失效
    $ pip install mistletoe
    import mistletoe
    html = mistletoe.markdown(text)
```

* sqlalchemy 插入数据报错
```
    百度说的Text默认6w字符 然后我没有填Text参数 
    最大的文章 5w多字符 写入时  error 1366 - Incorrect string value
    解决:  
        # config.db_text_count = 100000
        text = Column(Text(config.db_text_count))  
```

* 首页js加载 添加div元素时 滚动条不稳定回退
```
    解决:
        捕捉滚动条事件 记录滚动条坐标
        插入完成时 使用回到顶部的js代码
        修改成记录的坐标
```

* pending 待填
```
    在文章页面 音乐文件太大时 首次进入文章无错误
    第二次进入任意文章 状态就为pending 等6~10秒 
    而且 ajax失效 是重定向到目标页面
    服务器和客户端都是在本机 按我的理解 你去申请个MP3文件 
    带宽应该等于读写IO 又没有外网数据流通 
    区区10M的小文件 为何让我等那么久
    chrome浏览器显示的pending 服务器并没有收到申请
    就是说这个等待状态纯粹是在浏览器瞎等 
    等完了 服务器才收到get
    解决: 
        1. 不停的按刷新 可以控制在3秒内 但是
        2. 换个小的MP3文件 2M的珈百璃之歌 无pending
```

* 跨域访问 
```
    服务器太小了 在gitee上面挂了hexo 静态资源都一样
    申请资源时 转为get -> gitee 然后F12后台console两行黄色的
    小图片黄牌 超过1m的给红牌
    小资源能用就用吧 
    待填...
```

* 评论区
```
    取消了多层评论标签
    现在显示最多两层 原主题有多层标签关系 但是显示也是最多两层
    数据库里面还是保留有层级关系的
    不慌 反正没人评论 
    何时填 .. 需要填吗 
```

* logo
```
    本来想用numpy整个透明的logo
    后来打开发现图像shape居然是二维的 跟我之前打开miku图片不太一样 
    说好的三通道rgb不见了 而且还有个大问题
    为何透明和纯白都是用0存储的 计算机怎么区分呢 ?? 换换打出两个问号
    解决:
        百度在线ps第一个 
        图片拖进去 新建空白图层 
        魔术棒 选择空白区域 按键盘上的 delete 就没了 
        保存 告辞
```

* menu 
```
    还没写
```

* Gravatar头像
```
    它没有api 只要有email就能生成imgurl
    也不知怎么判断这个email到底有没有设置头像
    解决:
        用了别人的libgravatar库 pip直接装
        from libgravatar import Gravatar
        g = Gravatar(data['email'])
        g.get_image(default="404") # rtype http url
        
        用requests请求这个url 如果status_code 是404 
        就证明这个email没有设置头像 
        然后就可以不使用Gravatar 直接用我自定义的默认头像 
        整了1~8号的妹子图 随机抽一个
        
        app/status/img/number/[1-8].jpg
```

* JavaScript相关
```
    首页加载完毕时 (只有小圆点和首页图片)
    会调用一次new_json函数 获取文章列表 显示个数在config设置
```


