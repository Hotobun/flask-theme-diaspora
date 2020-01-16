---
title: Hexo diaspora主题增加搜索功能
date: 2020-1-04 15:01:41
tags: 
- blog
categories:
cover: /img/search.png
---

#### [github](https://github.com/Hotobun/hexo-theme-diaspora-search)

### 搜索引擎
搜索的本质就是寻找目标资源
网页常用的搜索
客户端提交表单->服务器查询数据库->返回数据到客户端
这种类型需要后台逻辑
 
***
### 静态网页怎么办 
网页做成之后 内容就无法改变 没有程序代码生成新数据
没有后台 不能写数据、常规的留言、访问次数 自身都做不了 想要只能调用外面的api

突然灵机一动 既然没有后台 就不要想动态处理的方式
前端不是有JavaScript吗 我们就用前端吧

*** 
### 原理
搜索页面先把所有文章标题都列举出来 
div标签设置隐藏 看上去就跟空标签一样
JavaScript捕捉搜索框输入的文本 
有了用户搜索的字符串 有了文章标题列表 
只要文章标题含有搜索文本的div 全部取消隐藏
这样 文章就显示出来了 
最后加个计数器 搜索完成

*** 
### 弊端
不适用太多数据 因为页面其实一开始就已经把所有文章列举出来的
我写的少 不慌 目测300篇内不出大问题

*** 
### 输入框
用了站长之家找的样式 稍作改动 还不错   
每按下一个按键 都能捕捉到 不需要按回车 取消了放大镜小图标  
[可扩展css3圆形搜索框](http://sc.chinaz.com/jiaoben/130222276600.htm)  

 


<form style=" text-align:center">    
    <style >
        input {
            outline: none;
        }
        input[type=search] {
            -webkit-appearance: textfield;
            font-family: inherit;
            font-size: 100%;
        }
        input::-webkit-search-decoration,
        input::-webkit-search-cancel-button {
            display: none;
        }
        input[type=search] {
            border: solid 1px #ccc;
            padding: 9px 9px 9px 9px;
            width: 200px;
            -webkit-border-radius: 10em;
            -moz-border-radius: 10em;
            border-radius: 10em;
            -webkit-transition: all .5s;
            -moz-transition: all .5s;
            transition: all .5s;
        }
        input[type=search]:focus {
            width: 130px;
            background-color: #fff;
            border-color: #6dcff6;
            margin-left: -11px;
            margin-right: 11;
            width: 330px;
            -webkit-box-shadow: 0 0 5px rgba(109, 207, 246, .5);
            -moz-box-shadow: 0 0 5px rgba(109, 207, 246, .5);
            box-shadow: 0 0 5px rgba(109, 207, 246, .5);
        }
        input:-moz-placeholder {
            color: #999;
        }
        input::-webkit-input-placeholder {
            color: #999;
        }
    </style>
    <script>
        function text_button_search_onkeypress(){
        var text = document.getElementById("search").value.toLowerCase();
        var p = document.getElementById("search_test");
        p.innerHTML = text;
        }
    </script>
    <input id = "search" name= "search" type="search" placeholder="积极开发中" 
    autocomplete="off" style="text-align:center" onfocus="this.setAttribute('placeholder', ''); " 
    onblur="if (this.value == '') this.setAttribute('placeholder', '下次一定！');" 
    onkeyup="text_button_search_onkeypress(),this.value=this.value.replace(/(^\s*)/g,'')">
    <input id = "search-btn" style="display: none;">
</form>

<span>检测到的文本: </span><span id = "search_test"></span>

***
### 食用方法
`gitbash` 下运行的  

``` bash
$ hexo new page search      #这行只是创建文件夹和index.md  
```
 
  
编辑Hexo的`source/search/`文件夹下的`index.md` 写入`type`   
 
```
---
title: search
type: "search"  
---
```

`themes/diaspora/layout/`文件夹下创建`search.ejs`

最后主题的_config.yml文件修改 menu

```
# 头部菜单，title: link
menu:
  主页: ''
  标签: /tags 
  归档: /archives 
  搜索: /search
```

<details>
  <summary> diaspora.js 文件末尾添加 </summary>

``` js
function get_posts(text){
    var posts = document.getElementsByClassName('timeline-item');
    // console.log(posts.length);
    if (text == ""){
        all_none(posts);
        return ;
    }
    var count = 0;
    for (var i = 0;i<posts.length; ++i){
        var temp = posts[i].id.toLowerCase();
        if ( temp.search(text) != -1 ){
            posts[i].style = "display: block";
            count += 1;
            // console.log(posts[i].id);
        } else {
            posts[i].style = "display: none";
        }
    }
    if (count > 0){
        var search_count = document.getElementById('search_count');
        search_count.style = "display: block";
        search_count.innerHTML = "为你献上"+count+ "篇"
    } else {
        document.getElementById('search_count').style = "display: none";
    }
}
function all_none(posts){
    for (let i = 0;i<posts.length; ++i){
        document.getElementById('search_count').style = "display: none";
        posts[i].style = "display: none";
    }
}
function button_search_onkeypress(){
    var text = document.getElementById("search").value.toLowerCase();
    // console.log("读取到的文本:"+ text );
    get_posts(text);
}
function text_button_search_onkeypress(){
    var text = document.getElementById("search").value.toLowerCase();
    var p = document.getElementById("search_test");
    p.innerHTML = text;
}
```

</details>  


<details>
  <summary> search.ejs 新建文件 </summary>

``` html
<div class="hexosearch">
    <style >
        input {
            outline: none;
        }
        input[type=search] {
            -webkit-appearance: textfield;
            font-family: inherit;
            font-size: 100%;
        }
        input::-webkit-search-decoration,
        input::-webkit-search-cancel-button {
            display: none;
        }
        input[type=search] {
            border: solid 1px #ccc;
            padding: 9px 9px 9px 9px;
            width: 200px;
            -webkit-border-radius: 10em;
            -moz-border-radius: 10em;
            border-radius: 10em;
            -webkit-transition: all .5s;
            -moz-transition: all .5s;
            transition: all .5s;
        }
        input[type=search]:focus {
            width: 130px;
            background-color: #fff;
            border-color: #6dcff6;
            margin-left: -11px;
            margin-right: 11;
            width: 330px;
            -webkit-box-shadow: 0 0 5px rgba(109, 207, 246, .5);
            -moz-box-shadow: 0 0 5px rgba(109, 207, 246, .5);
            box-shadow: 0 0 5px rgba(109, 207, 246, .5);
        }
        input:-moz-placeholder {
            color: #999;
        }
        input::-webkit-input-placeholder {
            color: #999;
        }
    </style>
</div>
<div style="margin-top: 123px;text-align:center">
        <form>
            <input id = "search" name= "search" type="search" placeholder="积极开发中" autocomplete="off" style="text-align:center" onfocus="this.setAttribute('placeholder', ''); " onblur="if (this.value == '') this.setAttribute('placeholder', '下次一定！');" onkeyup="button_search_onkeypress(),this.value=this.value.replace(/(^\s*)/g,'')">
            <input id = "search-btn" style="display: none;">
        </form>
</div>
 
<!-- 下面是归档代码 直接套过来 -->
<div id="single" class="page">
    <div id="top">
        <a class="icon-left image-icon" href="javascript:history.back()"></a>
    </div>
    <div class="section">
        <div class="article">
            <div class="main">
                <div class="content">
                    <div class="timeline">
                      <h2 style="display:none" class="timeline-title" id="search_count"></h2>
                      <% var posts = site.posts.sort('date', 'desc'); %>
                      <% for(let i = 0, year = -1; i < posts.data.length; ++i) { %>
                        <%
                          const psg = posts.data[i];
                          if(psg.date.year() !== year) {
                            year = psg.date.year();
                        %>
                        <% } %>

                        <% var text = "" %>
                        <% for(let i = 0; i < psg.tags.data.length; ++i) { %>
                            <%
                              text += "|";
                              text += psg.tags.data[i].name;
                            %>
                            <% } %>
                        <div style="display:none" class="timeline-item" id=<%= psg.title + text %> >
                          <time><%- psg.date.format("YYYY-MM-DD") %></time>
                          <a target="_self" href="<%- url_for(psg.path) %>"><%= psg.title %></a>
                        </div>
                      <% } %>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

```

</details>  
