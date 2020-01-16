---
title: Centos7挂酷Q机器人
date: 2019-12-20 16:12:28
tags: 
- QQ机器人
- linux 
categories:
cover: /img/coolq.jpg
---

看到破群里经常有机器人自动处理消息 自己也弄了一个。  
在windows上挂酷Q还行 服务器装酷Q各种问题 
按照教程一顿操作猛如虎 第一次就成功 然后我吧服务器重启了
熟悉的剧情出现了 这东西重启之后就用不了 
快照回滚了12次 终于找到一个重启能用的 
快照真是个好东西

### 安装docker
```
$ curl -sSL https://get.docker.com/ | sh
$ systemctl start docker
$ systemctl enable docker
# 此处安装完应该存快照 存快照 存快照
```
Docker 是一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的镜像中，然后发布到任何流行的 Linux或Windows 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口。

### 安装酷Q 
注意：不要尝试更改酷Q文件拥有者或者权限 不然会连接不上 
1. 下载酷Q 
`$ docker pull coolq/wine-coolq`  
2. 创建空文件夹存放酷Q数据
`$ mkdir /home/Hoto/coolq `  
3. 运行酷Q镜像
`$ docker run --name=coolq -d -p 8080:9000 -v /home/Hoto/coolq:/home/user/coolq -e VNC_PASSWD=hotcocoa -e COOLQ_ACCOUNT=3397937019 coolq/wine-coolq`  
    --name =coolq 为容器创建别名为 coolq
    -p 8080:9000  将外部8080接口映射到内部9000 # 测试过两个端口都9000会连接不上
    真实存放数据的linux路径:映射的windows容器路径
    后面3个就是密码、默认QQ、镜像名字随便写

### 常用命令
1. 查看酷Q运行日志 
    `$ docker logs coolq --tail 30`  # 数据量太多了 尽量加tail 
2. 启动和停止酷Q
    `$ docker start coolq`
    `$ docker stop coolq`
3. 查看所有镜像
    `$ docker images ` 
4. 查看正在运行的容器、查看所有容器
    `$ docker ps `
    `$ docker ps -a`

## 重装
``` bash
# 查看id
$ docker ps  
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
587c77c5faa4        coolq/wine-coolq    "/init.entrypoint st…"   10 seconds ago      Up 9 seconds        0.0.0.0:8080->9000/tcp   coolq

# 删除容器
$ docker rm 587c77c5faa4    
587c77c5faa4

# 运行酷Q镜像
`$ docker run --name=coolq -d -p 8080:9000 -v /home/Hoto/coolq:/home/user/coolq -e VNC_PASSWD=hotcocoa -e COOLQ_ACCOUNT=3397937019 coolq/wine-coolq`  
587c77c5faa4bfcca5bad9b1195806d1200764e0155bcbaafb905e327cc822ec    

```




