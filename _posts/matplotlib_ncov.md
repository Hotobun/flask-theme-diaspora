---
title: 2019 nCov疫情gif图片
date: 2020-1-27 21:01:38
tags: 
- Python
- Matplotlib 
cover: /img/ncov.jpg
---



<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/ncov_confirm.gif" alt=""> 
<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/ncov_dead.gif" alt=""> 
<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/ncov_suspect.gif" alt=""> 
<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/ncov_heal.gif" alt=""> 
  
 
 
``` python
from matplotlib import pyplot as plt 
from matplotlib import animation
from scipy import interpolate
import requests
import json, os, pickle
import numpy as np
# 实时全部信息
now_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=jQuery34109326359122726049_1580115460210&_=1580115460217'
 
# 历史信息
past_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts'
 
head = {
    'user-agent':'mozilla/5.0',
    # 'cookie':'',
    'referer':'https://news.qq.com//zt2020/page/feiyan.htm',
}
np_shape_num = 5
date = []
confirm = []
suspect = []
dead = []
heal = [] 
x,y = [],[]
 
def RequestsGetJson(url, filename):
    filename = filename+'.pkl'
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            r = pickle.load(f)
    else:
        r = requests.get(url, headers = head)
        with open(filename, 'wb') as f: 
            pickle.dump(r, f)     
          
    data  = r.text
    if 'jQuery34109326359122726049_1580115460210' in data:
        data = data[:data.rindex(")")]
        data = data.replace("jQuery34109326359122726049_1580115460210(", '') 
    # print(data)
    result = json.loads(data)
    result = json.loads(result['data'])
    return result
 
def past_data(show = True):
    result = RequestsGetJson(past_url, 'past')
    if show:
        print(result)
    return result
 
def now_data(show = True):
    data = RequestsGetJson(now_url, 'now')   
    count = {}
    for i in data:
        if i['country'] != '中国':
            continue
        # 确诊 治愈 死亡 总数统计
        count['confirm'] = count.get('confirm', 0) + i['confirm']
        # 疑似人数有误 不在这里抓
        # count['suspect'] = count.get('suspect', 0) + i['suspect'] 
        count['heal'] = count.get('heal', 0) + i['heal']
        count['dead'] = count.get('dead', 0) + i['dead']
    if show:
        print('确诊{}, 治愈{}, 死亡{} '.format(count['confirm'],count['heal'], count['dead']))
    return count
 
def lineshape(target, num = np_shape_num):
    # target type : [int,int...]
    # num type: int
    sumi = ( len(target)-1 ) * num + 1
    result = []
    for index in range(len(target)):
        item = target[index]
        result += [item]
        if len(result) < sumi:
             
            result += list(np.linspace(item, target[index+1], num=num-1))
    return result
 
def unit_plt(data, index=date, xmajor=1, ymajor=500, returnfilg=False):
    # index type: list 日期
    # data  type: list 该日期的数据
    # major type: int  对应xy轴的刻度范围 例 x隔一天一个刻度 
    ax = plt.gca()
    global x, y
    x += lineshape(index)
    y += lineshape(data) 
    if returnfilg:
        return (x, y)
    ax.xaxis.set_major_locator(plt.MultipleLocator(xmajor)) 
    ax.yaxis.set_major_locator(plt.MultipleLocator(ymajor)) 
    plt.plot(x, y)  
    plt.axis([ min(index), max(index), 0, max(data) + 10 ])
    plt.show()
 
def gif_init():
    global x,y 
    ax.set_title("新型冠状病毒nCoV 2020 1月 {}".format(text), fontproperties="Kaiti", fontsize = 14 )  
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(0,ylim)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1)) 
    ax.yaxis.set_major_locator(plt.MultipleLocator(y_major)) 
    return ln,
 
def gif_update( frame ): 
    global x,y   
    ln.set_data(x[:frame+1],y[:frame+1])
    return ln,
  
def gif(data):
    xy = unit_plt(data,returnfilg=True) 
    anim = animation.FuncAnimation(fig, gif_update, frames=range(len(xy[0])),interval=1,init_func=gif_init, blit=True, repeat_delay=22000)
    anim.save(filename)
    # plt.show()
 
if __name__ == "__main__": 
    past = past_data(show=False)
    past.sort(key= lambda x:x['date'])
 
    for item in past:
        date.append(int(item['date'][-2:]))
        confirm.append(int(item['confirm'] ))
        suspect.append(int(item['suspect'] ))
        dead.append(int(item['dead'] ))
        heal.append(int(item['heal'] )) 
     
    fig, ax = plt.subplots()
    ln, = plt.plot([],[],animated=True)
    plt.xlabel("数据来源: 腾讯新闻", fontproperties="Kaiti", fontsize = 14 ) 
    data_l = [
        # text  图标y轴最高值 y轴刻度步长 保存文件名 y轴数据
        ['全国确诊', max(confirm),   500, 'confirm.gif', confirm],
        ['死亡人数', max(dead),   10, 'dead.gif', dead],
        ['疑似病例', max(suspect),   500, 'suspect.gif', suspect],
        ['治愈人数', max(heal),   10, 'heal.gif', heal],
    ]
     
    for item in data_l:
        x,y = [],[]
        text = item[0]
        ylim = item[1]
        y_major = item[2]
        filename = item[3]
        if item[0] == '治愈人数':
            for i in range(len(item[4])):
                if item[4][i] == 0 and i > 4:
                    item[4][i] = (item[4][i-1] + item[4][i+1]) //2
        gif(data=item[4]) 
```