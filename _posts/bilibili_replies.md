---
title: 爬B站视频评论 
date: 2019-12-25 11:12:31
tags: 
- "mysql"
- "spider"
- "python"
categories:
cover: /img/bilibili_replies.jpg
---

#### [github源码](https://github.com/Hotobun/Code/tree/master/python/spider/bilibili/replies)
 
## 本地环境
- windows10 
- python
 
## 使用到的第三方库
- requests
- pymysql
- sqlalchemy
 
## 数据库
- mysql
 
## 食用方法
1. 填写config相关参数 数据库 htmlheaders 等...  
2. 第一次使用
```bash
进入mysql 创建数据库 已有库就在`config.py`里面改 :
`mysql> create database bilibili character set utf8 collate utf8_general_ci;`
参数 character set utf8 : 指定数据库采用字符集 不能使用utf-8
参数 collate : 指定数据库字符集的排序规则 通过show character set 查看
在终端运行或者直接打开`replies_db.py` 创建数据表
`$ python replies_db.py`
```   
3. 运行`replies_.py`  
 
*** 
续上篇 代码都差不多   
一个视频的评论量都是用万做单位 就没有遍历番号爬了  
记得在`config.py`填写oid 视频AV号  
文件保存是相对路径  
已请求的json都会保存到本地的AV号文件夹下面 留了3页做测试用  
再次请求时会先判断本地有没有这个json 如果有直接拿出来入库  
没有就去B站爬  
 
![](/img/archive_img/bilibili_replies.png)













