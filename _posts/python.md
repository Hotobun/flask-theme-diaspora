---
title: python 
date: 2019-12-04 23:34:16
tags: python 
categories: 基础 
cover: /img/python.jpg
---

## 进制转换：
* 二进制  bin()  
* 八进制  oct()  
* 十进制  int()  
* 十六进制  hex()  
* chr(x) # 返回十进制x对应的ASCII编码对应字符  
* ord(s) # 返回s字符对应的ASCII十进制编号  
* chr(97)   --> a  
* ord("A") --> 65  

*** 
## 根据文件创建时间排序指定目录下的文件名
```
target = os.getcwd()    # 获取当前目录
l = os.listdir(target)
a = l.sort(key = lambda x: os.path.join(target, x))
```

***

## 查找元素出现次数
``` python
import requests
r = requests.get("http://www.baidu.com")
d = dict()
for i in r.text:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for key,value in d.items():
    print("{}: {}".format(key, value))
```