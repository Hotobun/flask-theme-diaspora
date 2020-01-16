---
title: 爬天气数据绘图
date: 2020-1-09 21:01:00
tags: 
- spiser
- Matplotlib
categories:
cover: /img/weather.jpg
---

#### [github源码](https://github.com/Hotobun/weather)

## 爬取天气信息
数据来源 [tianqi.com](http://www.tianqi.com/)

## 使用到的库和工具
* requests
* sqlalchemy
* mysql
* pymysql 

## 使用
* 创建数据库 
  * CREATE DATABASE weather DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
* 填写`config.py`你家的数据库密码 
* 运行`spider.py`爬取数据 需要改城市可以修改url
* 运行`show_plot.py`输入年份月份 绘制图像 

![](/img/archive_img/weather1.png)
![](/img/archive_img/weather2.png)
