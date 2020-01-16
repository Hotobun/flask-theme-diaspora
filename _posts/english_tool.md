---
title: 工地英语学习工具
date: 2020-1-09 11:01:22
tags: 
- English
- python
- tkinter
- mysql
categories:
cover: /img/english_tool.jpg
---

[github源码](https://github.com/Hotobun/english_tool)

先放个图吧
![](/img/archive_img/english_tool1.png)
![](/img/archive_img/english_tool2.png)

***
## 功能
* 读取xlsx文件 写入数据库
* tkinter从数据库随机取5行数据显示出来
* 点击单词或句子 出现翻译

## 使用
* 进入mysql创建数据库
```
mysql> CREATE DATABASE english DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```
* 编辑`config.py`填写数据库接口
* 运行`db.py`写入数据
* 运行`tk.py`
  
## 遇到的坑
文本问题
终端是对齐的 到tkinter上就不齐了 待填
![](/img/archive_img/english_tool3.png)

## 语音
各大翻译平台调用语音api 门槛都很高 要不很贵 要不企业认证
迟点写个爬虫抓下来

