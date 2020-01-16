---
title: Hexo添加Valine评论系统
date: 2020-1-05 19:01:39
tags: 
- blog
- valine
categories:
cover: /img/valine.jpg
---

## 为什么用Valine 
不需要登录
其他评论系统全都要注册或者第三方平台账号
不是换评论系统 只是在首页右上角菜单 加一个留言板页面

*** 
## 使用方法

#### 创建valine文件夹及index.md
```
$ hexo new page valine
```
修改`source/valine/index.md` 添加type
```
---
title: valine 
type: "valine"
---
```

*** 
#### 修改`diaspora/layout/page.ejs`
添加valine那两行 
```
<% if (page.search || page.type === "search") { %>
    <%- partial('_partial/search') %>
<% } else if (page.type === "tags") { %>
    <%- partial('_partial/tags') %>
<% } else if (page.type === 'categories') { %>
    <%- partial('_partial/categories') %>
<% } else if (page.type === 'valine') { %>
    <%- partial('_partial/valine') %>
<% } else { %>
        <%- page.content %>
<% } %>
```

*** 
#### 新建文件`diaspora/layout/_partial/valine.ejs`
这几行代码只要在html中有个合适的位置插入即可
``` html
<div class="valine_comment"></div>
<script>
  var notify = '<%= theme.valine.notify %>' == true ? true : false;
  var verify = '<%= theme.valine.verify %>' == true ? true : false;
  new Valine({
      av: AV,
      el: '.valine_comment',
      app_id: '<%= theme.valine.appid %>',
      app_key: '<%= theme.valine.appkey %>',
      placeholder: '<%= theme.valine.placeholder %>'
    });
</script> 
```
*** 
#### 修改head.ejs
加载js文件
``` html
<head>
    <!-- head中间插入下面两条语句 -->
<% if (page.type === 'valine') { %><script src="//cdn1.lncld.net/static/js/3.0.4/av-min.js"></script> <% } %>
<% if (page.type === 'valine') { %><script src="//cdn.jsdelivr.net/npm/valine@1.1.9-beta9/dist/Valine.min.js"></script> <% } %>
</head>
```

*** 
#### LeanCloud
注册 登录[leancloud](https://www.leancloud.cn/) 
不喜欢实名可以用国际版 需要手机号、邮箱

创建应用 按提示填

进入应用 -> 设置 -> 安全中心 -> web安全域名 
填写自己域名

进入应用 -> 设置 -> 应用Keys
可以看到appid appkey 等信息

***
#### 配置文件
修改`diaspora/_config.yml`添加下面配置
详细配置参考[valine官网](https://valine.js.org/)
```
menu:
    ... 
  留言板: /valine
 
# 文件末尾添加valine配置
valine:
  enable: true      
  appid:  #  leancloud 
  appkey: #  leancloud 
  notify: true 
  verify: false  
  placeholder: 说点什么吧！ 
  avatar: hide 
  guest_info: nick # custom comment header
  pageSize: 10 # pagination size
  recordIP: false 
```


留言记录可以在 储存 -> Comment查看

