---
title: nginx端口转发
date: 2019-12-13 20:12:50
tags: 
- linux 
- nginx 
categories:
cover: /img/nginx.jpg
---
## 二级域名转发
已经部署两个网站
* `hotococoa.com`
* `hotococoa.com:9200`

早上尝试了下在`nginx.conf`只写两个`server`
80端口接收到指定域名时 转发到9200端口
请求是转过来了 但是请求的是主站目录  
不是9200网站目录 root也改几次 无果
后面发现有个二级域名的东西 尝试了下 居然一步到位

首先在阿里云后台打开域名->域名解析->添加记录
![](/img/archive_img/nginx.png)
![](/img/archive_img/nginx1.png)
添加完后编辑 `/etc/nginx/nginx.conf`
``` nginx
    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  hotococoa.com;
        root         /home/hexo;

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

    server {
        listen 80;                      
        root /home/nginx/flask-advance;
        index index.html index.htm;
        server_name flask.hotococoa.com;
        location / {
                try_files $uri $uri/ =404;
                proxy_pass http://127.0.0.1:9200; 
        }
        # 将80端口 flask.hotococoa.com 的请求 转发到9200
        # 如果不写这个server 请求flask.hotococoa.com 时就会匹配到上面的 hexo
    }
        # 最后 可以用二级域名访问 也可以用端口号访问
    server {
        listen 9200;
        listen [::]:9200;
        server_name flask.hotococoa.com;  # 这里填写刚刚创建的二级域名
        root 	/home/Hoto/flask-advance;

        location / {
            index	index.html index.html;
        }
    }
```

    

