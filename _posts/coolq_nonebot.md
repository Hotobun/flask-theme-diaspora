---
title: 酷Q机器人 基于NoneBot开发环境
date: 2020-1-30 19:01:11
tags: 
- coolq
- python
categories:
cover: /img/coolq_nonebot.jpg
---

## 为什么使用NoneBot 
> 人生苦短 我用python   

* NoneBot : 基于酷Q的Python异步QQ机器人框架 简介 易扩展 高性能
* 官方CQP sdk : 非法占用内存 估计也是数组越界 不是python的锅 不懂dll 已弃
* 原生易语言模块: 做界面很快 逻辑处理就一脸懵逼 语法贼复杂 习惯英文编程 看不懂中文语法 思路转不过来 已弃

## 环境
* CentOS 7
* Python 3.7.5 
* NoneBot 1.3.1
* Python 必须 >= 3.6 其他好像无所谓

## 原理如图
酷Q从服务器接收QQ消息 转发给NoneBot 处理过后再传给酷Q返回给腾讯  

![](/img/archive_img/coolq_nonebot_flow_chart.png)

## 配置Docker
安装Docker 略..
``` shell
# 下载酷Q官方docker镜像
$ docker pull coolq/wine-coolq
 
# 创建项目映射目录 备用
$ mkdir coolq
```

``` shell
# 安装酷Q容器
$ docker run -d --name coolq -d -p 9000:9000 -p 5700:5700 -v /home/Hoto/coolq:/home/user/coolq -e VNC_PASSWD=password -e COOLQ_ACCOUNT=12345678  -e CQHTTP_POST_URL=http://171.18.0.1:8080  -e CQHTTP_SERVE_DATA_FILES=yes coolq/wine-coolq
```
  
浏览器打开 服务器ip或域名:9000端口 可以看到noVNC 输入密码 就是刚刚的VNC_PASSWD    
进入后一顿操作 登录一次 开启一次http模块然后退出来    
  
回到服务器shell    
打开酷Q配置文件夹 一般在coolq/data/app/io.github.richardchien.coolqhttpapi/config/    
里面有刚刚登录过的 QQ号.json 打开修改下面3行 其他按需求填    
   

  
``` json
{
    "host": "[::]",
    "port": 5700,
    "use_http": true,
    "ws_host": "[::]",
    "ws_port": 6700,
    "use_ws": false,
    "ws_reverse_url": "",
    "ws_reverse_api_url": "ws://172.18.0.1:8080/ws/api/",    // 这里
    "ws_reverse_event_url": "ws://172.18.0.1:8080/ws/event/",// 这里
    "ws_reverse_reconnect_interval": 3000,
    "ws_reverse_reconnect_on_code_1000": true,
    "use_ws_reverse": true,   // 这里
    "post_url": "",
    "access_token": "",
    "secret": "",
    "post_message_format": "string",
    "serve_data_files": false,
    "update_source": "china",
    "update_channel": "stable",
    "auto_check_update": false,
    "auto_perform_update": false,
    "show_log_console": true,
    "log_level": "info"
}
```
#### 重点 要考的  
ip如果不通 记得先测试 哪个ip通网填哪个 官方配置在linux是行不通的     
``` sh
# 用下面两条命令都可以查看ip
$ ifocnfig
$ ip addr
  
# 容器ip 172.18.0.2   
# 主机ip 172.18.0.1  
```
这里填的是酷Q向Nonebot请求的ip NoneBot部署在172.18.0.1   
 
 
配置过后 再次浏览器打开 ip:9000 进入noNVC  
运行酷Q 登录 启用http插件  

## git相关
ssh免密码 略..  不需要git的略..
 
服务器
```
# 视情况该路径
# 创建裸仓库
$ git init --bare nonebot.git
  
# 创建钩子文件 nonebot.git是仓库 mybot是本地push后文件映射到服务器的路径 
$ vim nonebot.git/hooks/post-receive
# /bin/sh
git --work-tree=/home/Hoto/cocoa/mybot --git-dir=/home/Hoto/cocoa/nonebot.git checkout -f
  
# 添加执行权限
$ chmod +x nonebot.git/hooks/post-receive
```
本地Windows 
```
# 创建仓库 已有就略..
$ git init
$ git add .
$ git commit -m "firsh commit"
  
# user视情况填 不是全都用git用户 这里踩了个坑 以为是git语法 
$ git remote add origin Hoto@hotococoa.com:/home/Hoto/cocoa/nonebot.git
  
$ git push -u origin master
```

## NoneBot
```  shell
# 安装虚拟环境 这里使用pipenv
# 命令行直接装 详细配置查看官网
$ pip install pipenv 
 
# 进入mybot目录 创建环境 
$ cd mybot
$ pipenv install
 
# 安装依赖 有几个需要的库不会自动装 
# 报warning再弄吧 也不出错 弄不懂到底需不需要 反正能用
$ pipenv install msgpack
$ pipenv install ujson
$ pipenv install requests
$ pipenv install nonebot
 
# 运行
$ pipenv run python bot.py 
 
# 运行不等于挂机 你退出shell就没了 测试过代码没问题后 
# 用下面命令 不间断+后台+运行
$ nohup pipenv run python bot.py &
 
# 查看网关 
$ netstat -tnlp 
 
# 查看nohup运行日志 看到有 GET /ws/xxx/ 101 就连接成功 
# 没就慌了 检查ip 写几个socket测试通不通网 这里我卡了半天
$ tail -n 50 nohup
```
![](/static/img/archive_img/coolq_nonebot_nohup.png)

如果有两个 GET /ws/xxx/ 101  说明已经配置完成了 
剩下就是开发插件的事了 现有的插件丢上去都能用  

## 一堆坑

## 提示缺少 Windows Script Control组件
这是由于 Wine 对部分组件支持不完全造成的  
通过 Winetricks 安装 msscript 及 winhttp 组件即可
右击空白调出菜单 进入命令行 下面3条命令 运行完就ok
```
$ wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
$ chmod +x winetricks
$ sh winetricks msscript winhttp
```

## nonebot __init__ error
本来是按原教程操作的 Windows上一切正常  
部署上云后各种问题 毕竟是linux 没有原生windows环境  
首先 项目目录里的config.py 写了如下参数
``` python
# 看上去很正常
PORT = 8080
HOST = '127.0.0.1'
```
然后 运行bot.py时报错 
```
__init__ got an unexpected keyword argument host
```
查看源码 也没看出问题 
```
# NoneBot/__init__.py line 25-26
super().__init__(message_class=aiocqhttp.message.Message,
        **{k.lower(): v for k, v in config_dict.items()})
```
最后一顿操作测试 
```
# print() 成功输出两个config.py中的值 证明这个字典正确
print(config_dict['PORT'],config_dict['HOST'])

# 删掉 **{dict ... } 没报错
super().__init__(message_class=aiocqhttp.message.Message)

# 关键字参数  同样报错
super().__init__(message_class=aiocqhttp.message.Message,
            host='172.18.0.1', port=8080)
```
结论 这个__init__就不能传ip端口进去 直接写的传关键字都报错   
解决：
* 注意括号 删掉 **{k.lower(): v for k, v in config_dict.items()}
* 如果要修改端口和ip去 nonebot目录 default_config.py修改

尝试运行
```
$ pipenv run python bot.py
```
成功 看到等待会话状态   
但这只能使nonebot运行起来 并不保证与酷Q连接 这两部分是独立的  
 
## 连接酷Q
巨坑    
在容器的noNVC 右键菜单 打开命令行    
ip addr 查看ip 显示 172.18.0.2  
 
主机对应ip 172.18.0.1  
 
此处 应该修改前面说的 default_config.py   
因为项目目录写的config.py 在__init__.py 读入会报错啊   

```
# nonebot库目录/default_config.py  line 25-26
HOST: str = '127.0.0.1'
PORT: int = 8080
 
# 修改为
HOST: str = '172.18.0.1'
PORT: int = 8080
```
这两个是nonebot绑定监听的ip端口 nonebot就在这里 可以看前面绘图  
nonebot到这里基本配置完毕 

docker容器方面 
