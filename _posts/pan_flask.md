---
title: Flask+HDFS云盘系统
date: 2019-12-28 17:12:23
tags: 
- hadoop
- python
- 网盘
categories:
cover: /img/pan_flask.jpg
---

[参考github](https://github.com/seeicb/Flask-Disk)  
路过发现flask云盘开源项目    
点进去逛了一圈 Hadoop连接居然失效了！  
花了两天啃了Hadoop知识 粗略了解了下  
已知问题：  
* 内存不足会蹦 NameNode自动关闭   
  

1核1G的虚拟机 还是太折腾了 已经挂了两个静态网站和一个qq机器人 机器人退下了才挂的稳  
![](/img/archive_img/pan_flask_top.png)

*** 
## 环境
* 阿里云 CentOS 7 
* java Hadoop ...
* python Flask ...
* 创建了一个flask用户

***
## 安装 java 
[java jdk官网](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)  
我这里用的rpm安装 注册就可以下载了 复制下载地址
![](/img/archive_img/pan_flask_java.png)
``` bash
$ wget file_url
$ rpm -ivh file.rpm
 
# 查看java版本
$ java -version
java version "1.8.0_231"
Java(TM) SE Runtime Environment (build 1.8.0_231-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.231-b11, mixed mode)
 
# java默认安装目录 
$ ls /usr/java
default  jdk1.8.0_231-amd64  latest
```

***
## 安装Hadoop
[Hadoop官网](https://hadoop.apache.org/releases.html)
![](/img/archive_img/pan_flask_hadoop.png)
下载完之后 解压在`/home/flask`目录下然后改个名  
`$ mv hadoop-2.10.0 hadoop  `

### 设置ssh免密码登录 (跳过也可以 每次连接都需要密码)
``` bash
$ cd ~
 
$ ssh-keygen -t rsa -P''-f〜/ .ssh / id_rsa  
$ cat〜/ .ssh / id_rsa.pub >>〜/ .ssh / authorized_keys  
$ chmod 0600〜/ .ssh / authorized_keys
 
# 查看可否无密码登录
$ ssh localhost
```

### 配置Hadoop
``` bash
$ cd /home/flask/hadoop/etc/hadoop
```

修改 hadoop-env.sh
```bash
# The java implementation to use.
# export JAVA_HOME=${JAVA_HOME}    # java目录
export JAVA_HOME=/usr/java/jdk1.8.0_231-amd64
 
# 文件最后加上这句
export HADOOP_OPTS="$HADOOP_OPTS -Djava.net.preferIPv4Stack=true -Djava.library.path=$HADOOP_HOME/lib:$HADOOP_COMMON_LIB_NATIVE_DIR"
```
 
修改 core-site.xml  
填内网ip 临时文件夹 记得先建立文件夹  
```html
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://172.17.29.48:9003</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/home/flask/data/tmp</value>
    </property>
    <property>
        <name>fs.trash.interval</name>
        <value>10080</value>
    </property>
</configuration>
```
 
修改 hdfs-site.xml  
同样先创建填写的文件夹  
```  html
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/home/flask/data/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/home/flask/data/data</value>
    </property>
</configuration>
```

格式化文件系统
``` bash
$ bin/hdfs namenode -format
```

启动/关闭 NameNode和DataNode 
```bash
# 没配置ssh要输入三次密码
$ sbin/start-dfs.sh
$ sbin/stop-dfs.sh
```

查看进程
```bash
$ jps
9826 DataNode
12596 Jps
10023 SecondaryNameNode
9722 NameNode
```

没有配置YARN 因为启动YARN NameNode就崩了   
阿里云后台 防火墙开放50070端口 就可以在浏览器上访问ip:50070的web界面了

*** 
## 添加环境变量
`$ vim /etc/profile `   
``` bash
export JAVA_HOME=/usr/java/jdk1.8.0_231-amd64
export PATH USER LOGNAME MAIL HOSTNAME HISTSIZE HISTCONTROL
export HADOOP_HOME=/home/flask/hadoop
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH::$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOOME/sbin:$HADOOP_HOME/lib
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"
```


***
## 搭建Flask
virtualenv虚拟环境 
``` bash
$ pip3 install virtualenv
$ virtualenv --version
16.7.9
 
$ virtualenv --no-site-packages /home/flask/pan
$ source /home/flask/pan/bin/activate

```
在虚拟环境下安装项目依赖  
后续 [参考原文](https://github.com/seeicb/Flask-Disk)

***
## 上云
推荐在virtualenv 环境下部署  
### nginx添加映射 
公网访问hotococoa.com:23456 就转发到服务器23432  
`$ vim /etc/nginx/nginx.conf`
``` bash
https{
    ...
    server {
        listen 23456;
        server_name hotococoa.com;
        
        location / {
                include         uwsgi_params;
                uwsgi_pass      127.0.0.1:23432;
                uwsgi_param  UWSGI_PYHOME /home/flask/pan;
                uwsgi_param  UWSGI_CHDIR  /home/flask/Flask-Disk;
                uwsgi_param  UWSGI_SCRIPT flask_web:application;
                uwsgi_read_timeout 300;
                uwsgi_connect_timeout 300;
                uwsgi_send_timeout 300;
        }
    }
    ....
}
```

### uwsgi.ini   
安装:  
`$ pip install uwsgi`
修改`uwsgi.ini`
``` bash
[uwsgi]
master = true
home = /home/flask/pan
wsgi-file = manage.py
callable = app
socket = :23432
processes = 4
threads = 2
buffer-size = 32768
```

### 部署
``` bash 
# 检查nginx.conf语法
$ nginx -t 
 
# 重启nginx生效
# nginx -s reload
 
# uwsgi 后台静默运行 不添加的话 关闭服务器连接进程就没了
$ nohup uwsgi --ini uwsgi.ini &

```

### 关闭 
```
# 找到uwsgi进程pid
$ lsof -i :23432 

$ kill -9 pid

# 查看nohup.out 还挺皮的
...
uWSGI worker 1 screams: UAAAAAAH my master disconnected: i will kill myself !!!
uWSGI worker 2 screams: UAAAAAAH my master disconnected: i will kill myself !!!
uWSGI worker 3 screams: UAAAAAAH my master disconnected: i will kill myself !!!
uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
uWSGI worker 1 screams: UAAAAAAH my master disconnected: i will kill myself !!!
uWSGI worker 2 screams: UAAAAAAH my master disconnected: i will kill myself !!!
uWSGI worker 3 screams: UAAAAAAH my master disconnected: i will kill myself !!!
uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
```