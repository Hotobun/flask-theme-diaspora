import os
from lxml import etree
from app.database import db

with open("text_comment.html",  'r', encoding='utf-8') as f:
    data = f.read()

t = etree.HTML(data)

a = t.xpath("//ol[@class='comment-list']/li")

data = []
l = []

for item in a:
    id = item.xpath("./@id")[0].replace('comment-', '')
    author = item.xpath("./div/div/cite/text()")
    date = item.xpath("./div/div/a/text()")[0].replace("\n", ' ').strip()
    text = item.xpath("./div/p/text()")[0]
    img = item.xpath("./div/div/img/@src")[0]
    root = 0
    site = item.xpath("./div/div/cite[@class='fn']/a/@href")
    if site:
        site = site[0]
    else:
        site = ''

    if len(author) < 1:
        author = item.xpath("./div/div/cite/a/text()")
    author = author[0]
    b = item.xpath(".//ol/li") 
    for i in b:
        croot = id
        cid = i.xpath("./@id")[0].replace('comment-', '')
        cauthor = i.xpath("./div/div/cite/text()")
        cdate = i.xpath("./div/div/a/text()")[0].replace("\n", ' ').strip()
        ctext = i.xpath("./div/p/text()")[0]
        cimg = i.xpath("./div/div/img/@src")[0]
        csite = i.xpath("./div/div/cite[@class='fn']/a/@href")
        if csite:
            csite = csite[0]
        else:
            csite = ''
        if not cauthor:
            cauthor = i.xpath("./div/div/cite/a/text()")
        cauthor = cauthor[0]
        # print(csite)
        # print(cid, cauthor, cdate, ctext, cimg) 
        data.append([cid, croot, cauthor, cdate, ctext, cimg, csite])
    data.append([id, root, author, date, text, img, site])
    # print(site)

for d in data:
    new = {
        "id":d[0],
        "root":d[1],
        "author":d[2],
        "date":d[3],
        "comment":d[4],
        "vcardurl":d[5],
        "site":d[6],
        "email":'',
        "fid":'invest'
    }
    # if int(new['id']) == 64631:
    #     continue
    db.insert_comment(new)
    print(new)
    # print("id", new['id'], new['author'], new['text'])
print(len(data))
    
