import os, sys
sys.path.append(".")
import markdown 
from app.setting import config
from app.database import db
import mistletoe

archive_path = config.archive_path

def get_archives():
    # 遍历文件夹下面的所有md文件
    archives = []
    queue = os.listdir(archive_path)[::-1]
    while queue:
        new = queue.pop()
        # print("new --> ", new)
        if new[-3:] == ".md":
            archives.append(new)
            continue
        elif os.path.isdir(os.path.join(archive_path,new)):
            for temp in os.listdir(os.path.join(archive_path,new)):
                # print('temp --> ',  temp)
                queue.append(os.path.join(new, temp))
    # print("archives", archives)
    # print(len(archives))
    return archives

def items():
    # 返回插入sql的数据
    for filename in now_archives:
        with open(os.path.join(archive_path,filename), 'r', encoding='utf-8') as f: 
            if f.readline().strip() == "---": 
                flag = 1
                headlist = []
                while flag:
                    newline = f.readline()
                    if newline.count("-") >= 3:
                        flag = 0
                        break
                    else:
                        if newline.count(":") >= 1:
                            key = newline[:newline.index(':')].strip()
                            value = newline[newline.index(':') + 1:].strip()
                            headlist.append([key, value])
                        elif '-' in newline and newline[0] == '-':
                            headlist[-1][-1] = headlist[-1][-1].strip() + ' ' + newline[1:].strip()
                            headlist[-1][-1] = headlist[-1][-1].strip()
                abstract = ''
                l = False
                text = f.read()
                text = text.replace("](/img/archive_img", '](/static/img/archive_img')
                m = markdown.markdown(text[:200]) 
                for i in m:
                    if i == "<"  :
                        l = True
                    elif i == ">" :
                        l = False
                        continue
                    if l or i in "\n*`":  
                        continue
                    abstract += i
                headlist.append(["text", mistletoe.markdown(text)])
                headlist.append(["abstract", abstract[:80]])
                headlist.append(['filename', InitSqlFilename(filename)  ])
                yield dict(headlist)

def update_sql():    
    # flag = True
    # filenames = [InitSqlFilename(name) for name in now_archives]
    # db.update_archives(filenames)
    # exit()
    for item in items():
        # print(item["filename"])
        # print("item --> ", item)
        # if flag:
            # 先删除表 再更新数据 可能存在很多细微改动 推到重写方便
            # db.drop_table('archive')
            # flag = False
        db.insert(item)
        # if item['filename'] == "english":
        #     temp = item['text']
        #     for i in temp.split("\n"):
        #         print(i)
        #         item['text'] = i
        #         db.insert(item)
         
        pass
    print("更新完成")

def InitSqlFilename(s):
    # 格式化用于数据库里的文件名
    # 例如 python/hello.md  --> python_hello 
    return s.replace('.md', '').strip().replace("\\", '/').replace("/", "_")

def main():
    update_sql()
    # a = db.query_archive('python',1)
    # for i in a:
    #     print(i)

if __name__ == "__main__":
    db.Create_table()
    now_archives = get_archives()
    main()
    # print(get_archives())