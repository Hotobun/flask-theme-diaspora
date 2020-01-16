---
title: flask移植diaspora主题
date: 2020-1-11 15:01:55
tags: 
- 
categories:
cover: 
---




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

