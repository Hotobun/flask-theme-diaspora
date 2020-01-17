---
title: 爬取B站所有番剧入库MySql
date: 2019-12-23 17:12:41
tags: 
- mysql
- spider
- python
categories:
cover: /img/bilibili_anime.jpg
---
 
#### [github源码](https://github.com/Hotobun/Code/tree/master/python/spider/bilibili/anime)
## 本地环境
- windows10 
- python 
 
## 使用到的第三方库
- requests
- pymysql
- lxml
- sqlalchemy
 
## 数据库
- mysql
 
## 食用方法
1. 填写config相关参数 数据库 htmlheaders 等...  
2. 第一次使用   
``` bash
进入mysql 创建数据库:  
`mysql> create database bilibili character set utf8 collate utf8_general_ci;`  
参数 character set utf8 : 指定数据库采用字符集 不能使用utf-8  
参数 collate : 指定数据库字符集的排序规则 通过show character set 查看  
在终端运行或者直接打开`bilibili_db.py` 创建数据表  
`$ python bilibili_db.py`  
```
3. 运行`blibili_anime.py`

 
*** 
没什么防爬机制 f12查看Network   
发现bilibili.com/...page=1... 里面有一页的20条数据   
page+1 就是下一页  
headers 复制过来 然后就愉快地爬了   
 
pkl文件夹里面的内容是每一页`requests.get(url)` 返回的`response`对象   
喜欢的话可以打开查看 是一堆json  
``` python
# 2019-12-23
import pickle
with open("pkl/page1.pkl", 'rb') as f:
    response = pickle.load(f)
```
 
![](/img/archive_img/bilibili_spider1.png) 
![](/img/archive_img/bilibili_spider2.png)
