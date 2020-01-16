---
title: 本站的坑
date: 2019-12-09 23:23:33
tags: blog
categories: 
cover: /img/blog.png
---

## 部署
#### 本地环境：
* windows10
* 环境:git, Node.js, hexo...
* 生成本地静态网站

#### 服务器环境：
* 阿里云 centos7
* 环境: git, Nginx, 创建git用户 略...
* 使用git自动化部署
* `yum install git`
* `yum install nginx` 略..

#### 秘钥配置  
本地使用windows gitBash
`ssh-keygen -t rsa` 
可以不用填 直接回车三连 
看到下图大概ok
```  
$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/cocoa/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/cocoa/.ssh/id_rsa.
Your public key has been saved in /c/Users/cocoa/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:aVu4RvVva6KAlg6j7IOrjxzUjjMPD8MJfZbRYzCVkDo cocoa@Hoto
The key's randomart image is:
+---[RSA 3072]----+
|    ++..         |
|    .+.          |
|   .. +   .      |
| .E  + . + .     |
|...o+   S . .    |
|+ +o   = +   .   |
| % .o + =     o  |
|oo@. = . .  .... |
|===+  .   .. o.  |
+----[SHA256]-----+
```
windows gitBash 有如下文件 known_hosts保存旧秘钥的 不需要可以删掉 
```
$ ls ~/.ssh
id_rsa  id_rsa.pub  known_hosts
```
在服务器上 切换至git用户
`mkdir ~/.ssh`  
`vim ~/.ssh/authorized_keys`
将本地`id_rsa.pub`文件内容粘贴到服务器`authorized_keys`里面
修改权限
`cd ~`
`chmod 600 .ssh/authorzied_keys`
`chmod 700 .ssh`

#### 测试
在本地windows上 使用`GitBash`测试是否能连接上服务器
`ssh -v git@serverip`
如果有错误提示 删除本地`known_hosts`文件里面纪录的服务器相关信息

#### nginx
安装 `yum install nginx` 过程略...
使用 nginx -t 命令查看位置，一般为 /etc/nginx/nginx.conf    
使用 vim /etc/nginx/nginx.conf 命令进行编辑，修改配置文件如下：  
```
server {
    listen       80 default_server;
    listen       [::]:80 default_server;
    server_name  www.hotococoa.com;    # 修改为自己的域名
    root         /home/hexo;    # 修改为网站的根目录

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

    location / {
    }
    error_page 404 /404.html;
        location = /40x.html {
    }
    error_page 500 502 503 504 /50x.html;
        location = /50x.html {
    }
}
```
`root`为网站目录 就是部署上传的位置
使用`nginx -t`检查配置语法
`systemctl restart nginx.service`重启nginx 
完.


*** 
## 评论区的坑
#### 创建一个新仓库
记住这个仓库名字 
![](/img/archive_img/blog_pit1.png)

#### 创建GitHub Application
没创建的 [点这里申请](https://github.com/settings/applications/new)  
已创建的在`Settings` -> `Developer settings` -> `OAuth Apps`里面找  
这个名字貌似随便填 反正没用上  
![](/img/archive_img/blog_pit2.png)


#### 填写config

``` bash
# Gitalk 评论插件（https://github.com/gitalk/gitalk）
gitalk:
    # 是否自动展开评论框
    autoExpand: false
    # 应用编号
    clientID: '2275782fd492bd7192d5'  # 步骤2 
    # 应用秘钥
    clientSecret: '4bdaa80e28e4a5764b22cae20807e6c39ff3be4d'   # 步骤2
    # issue仓库名
    repo: 'HexoGitalk'   # 步骤1 
    # Github名
    owner: 'Hotobun'     # 后面自己填 
    # Github名
    admin: ['Hotobun']
    # Ensure uniqueness and length less than 50hexo  
    id: location.pathname
    # Facebook-like distraction free mode
    distractionFreeMode: false

```

*** 
## 修改表格宽度
``` css
# diaspora.css line 220
# 修改 table-layout 
# 源文件
.content table {margin:15px 0;border-collapse:collapse;display:table;width:100%;table-layout:fixed;word-wrap:break-word;}
 
# 修改后
.content table {margin:15px 0;border-collapse:collapse;display:table;width:100%;table-layout:automatic;word-wrap:break-word;}
```

![](/img/archive_img/blog_table1.png)
![](/img/archive_img/blog_table2.png)