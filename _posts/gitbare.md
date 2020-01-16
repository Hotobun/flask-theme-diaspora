---
title: Git裸仓库
date: 2019-12-14 15:12:50
tags: 
- git
- linux
categories:
cover: /img/gitbare.jpg
---

[git钩子文档](https://git-scm.com/book/zh/v2/自定义-Git-Git-钩子)  
***

###  建立git裸仓库
创建一个裸仓库 只保存`git`信息的`Repository`
切换到git用户有有仓库所有权 
一定要加 `-- bare` 这样才是裸库
``` git
$ su root 
$ cd /home/git
$ git init --bare blog.git
```
这时 `git`用户的`~`目录下就存在一个`blog.git`文件夹  
可使用`ls`查看 再修改 `blog.git`权限  
`$ chown git:git -R blog.git`

### 使用git-hook 同步网站根目录
这里使用`post-receive`这个钩子 当`git`有手法的时候会调用这个钩子  
在`blog.git`裸库hook文件夹中 新建`post-receive`文件
`$ vim blog.git/hooks/post-receive`
填入一下内容 其中`/home/hexo`为网站根目录
``` git
#! /bin/sh
git --work-tree=/home/hexo --git-dir=/home/git/blog.git checkout -f
```
保存后 赋予这个文件可执行权限
`$ chmod +x /home/git/blog.git/hooks/post-receive`

***