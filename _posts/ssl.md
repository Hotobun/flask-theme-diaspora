---
title: ssl证书配置
date: 2019-12-25 10:12:32
tags: 
- linux 
categories:
cover: /img/ssl.png
---
  
下载申请的证书 随便放 记住位置  
我这里放到`/etc/nginx/cert/`目录下   
编辑`/etc/nginx/nginx.conf`  
``` bash  
https{
...
    server { # 在已部署好的server 添加rewrite 请求都跳转到https
        listen    80;
        rewrite ^(.*)$ https://$host$1;
        ....
    }
    
    server {  # 新增server 443为https默认端口
        listen 443 ssl;
        server_name hotococoa.com www.hotococoa.com;
        root        /home/hexo;

        ssl_certificate /etc/nginx/cert/hotococoa.pem;   #name.pem替换成您证书的文件名。
        ssl_certificate_key /etc/nginx/cert/hotococoa.key;   #name.key替换成您证书的密钥文件名。
        ssl_session_timeout 5m;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;
        location / {
        index index.html index.htm;
        }
    }
    
}
```

```
$ nginx -t # 检查语法正确性
$ nginx -s reload # 重启nginx
```


