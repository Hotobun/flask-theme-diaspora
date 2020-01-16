---
title: python爬妹子图
date: 2019-12-22 19:12:47
tags: 
- python
categories:
cover: /img/meizispider.jpg
---
 
偶尔看点妹子养养眼吧
防爬机制只有referer 而且是当前页面的url
![](/img/archive_img/meizi.png)
 
``` python
import requests
from lxml import etree
import os, time
 
url = "https://www.mzitu.com/japan/page/"
head = {
    "user-agent":"Mozilla/5.0",
    "referer":"https://www.mzitu.com"
}
 
# 图片保存路径 不存在就创建
imgpath = os.path.join(os.getcwd(),'meizitu')
if not os.path.exists(imgpath):
    os.mkdir(imgpath)
# 每张图片请求间隔 已测试0.3爬原图会图片不全 爬封面的话0也可以
timeout = 0.5
# 仅爬取封面 False为爬取全图 大量图 小心身体
is_cover = True
 
def page_item(url, head):
    # rtype = [[title,imgurl,referer, imgsIdurl]...]
    r = requests.get(url, headers= head)
    t = etree.HTML(r.text)
    result = []
    for i in t.xpath("//ul[@id='pins']/li"):
        title = i.xpath("./a/img/@alt")[0].replace("?", '')
        imgurl = i.xpath("./a/img/@data-original")[0]
        idurl = i.xpath("./a/@href")[0]
        item = [title, imgurl, url,idurl]
        result.append(item)
    return result
 
def get_cover_img(imgitem):
    # imgitem type = [title,imgurl,referer, imgsIdurl] 
    head['referer'] = imgitem[2]
    imgname = imgitem[0].replace('?','') + '.jpg'
    save(imgitem[1], os.path.join( imgpath, imgname ), head)
 
def get_origin_img(imgitem):
    # imgitem type = [title,imgurl,referer, imgsIdurl] 
    head['referer'] = imgitem[2]
    r = requests.get(imgitem[3], headers = head)  
    t = etree.HTML(r.text)
    max_page = int(t.xpath("//div[@class='pagenavi']/a/@href")[-2].split('/')[-1])
    imgsrc = t.xpath("//div[@class='main-image']/p/a/img/@src")[0]
    head['referer'] = imgitem[3]
    for page in range(1, max_page+1):
        new_imgsrc = imgsrc.replace('01.jpg', "{0:02d}.jpg".format(page))
        imgname = imgitem[0] + str(page) + '.jpg'
        save(new_imgsrc, os.path.join(imgpath, imgname), head)
 
def save(url, path, head):
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)
        print(path, 'done')
    time.sleep(timeout)
     
def main():
    global head
    for page in range(1,30):
        for item in page_item(url+str(page)+"/", head = head):
            if is_cover:
                get_cover_img(item)
            else:
                get_origin_img(item)    
 
if __name__ == "__main__":
    main()
```
