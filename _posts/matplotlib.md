---
title: Matplotlib
date: 2020-1-06 23:01:01
tags: 
- Matplotlib
categories:
cover: /img/matplotlib.jpg
---

## 第一个Matplotlib程序
``` python
import matplotlib.pyplot as plt 
 
plt.plot([3,1,4,5,2])   
plt.ylabel("Grade")     # 标签名
plt.savefig("test",dpi=600) 
```
* savefig 参数:
  * filename : 保存的文件名 默认是png 也可以指定格式保存
  * dpi: 输出文件的质量 每一英尺空间中包含点的数量
可以查看输出的`test.png`图像
![matplotlib1](/img/archive_img/matplotlib1.png)


#### 输入多个列表
``` python
import matplotlib.pyplot as plt 
 
plt.plot([0,2,4,6,8],[3,1,4,5,2])   
plt.ylabel("Grade")     # 标签名
plt.axis([-1,10,0,6])
plt.savefig("test1",dpi=600)
```
* plot参数：
  * 当有多个列表时 分别对应x轴与y轴的点
  * XY: (0,3) (2,1) (4,4) (6,5) (8,2)
* axis参数:
  *  需要4个变量的列表 对应画图区域
  *  x轴起始于-1 终止与10
  *  y轴起始于0 终止与6
![matplotlib2](/img/archive_img/matplotlib2.png)

*** 
## pyplot的绘图区域
分隔绘图区域使用函数subplot
* plt.subplot(nrows, ncols, plot_number)
  * 3个参数都是int类型
  * nrows: 横轴数量
  * ncols: 纵轴数量
  * plot_number: 绘图子区域编号 所有绘图都在这个子区域进行
  * 由于全是数字可以简写一个参数 plt.subplot(3,2,4) 可以简写为 plt.subplot(324)


``` python 
import matplotlib.pyplot as plt 
import numpy as np 
 
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
 
if __name__ == "__main__":
    a = np.arange(0.0, 5.0, 0.02)
    plt.subplot(211)        # 将绘图区域分为2行1列 选择第一块
    plt.plot(a, f(a))
 
    plt.subplot(2,1,2)      # 将绘图区域选择为2行1列的第二块
    plt.plot(a, np.cos(2*np.pi*a), 'r--') # r-- 表示虚线绘制
    plt.show()
```
![matplotlib3](/img/archive_img/matplotlib3.png)

*** 
## plot函数
* plt.plot(x, y, fromat_string, **kwargs)
  * x : X轴数据, 列表或数组, 可选。当绘制多条曲线时, x不能省略
  * y : Y轴数据, 列表或数组.
  * format_string : 控制曲线的格式字符串, 可选。
  * **kwargs : 第二组或更多(x, y, fromat_string) 
    * color : 控制颜色, color = "green"
    * linestyle : 线条风格, linestyle = "dashed"
    * marker : 标记风格, marker = 'o'
    * markerfacecolor : 标记颜色, markerfacecolor = "blue"
    * markersize : 标记尺寸, markersize = 20
    * ...

尝试画4条曲线
```python
import matplotlib.pyplot as plt 
import numpy as np 
 
if __name__ == "__main__":
    a = np.arange(10)
    plt.plot(a, a*1.5,a, a*2.5, a, a*3.5, a, a*4.5) # 注意这里是8个参数 每两个一组
    plt.show()
```

![matplotlib4](/img/archive_img/matplotlib4.png)

format_string 参数由颜色字符、风格字符和标记字符组成  
如果不选择颜色 Matplotlib会为不同曲线选择唯一的颜色区分

颜色字符|说明|颜色字符|说明 
:--|:--|:--|:--
'b'|蓝色|'m'|洋红色magenta
'g'|绿色|'y'|黄色
'r'|红色|'k'|黑色
'c'|青绿色|'w'|白色
'#123321'|用户控制颜色|0.8|灰度值字符串


风格字符|说明 
:--|:--
'\-'|实线
'\-\-'|破折线
'-.'|点划线
':'|虚线
''|无线条

标记字符|说明 |标记字符|说明 |标记字符|说明 |
:--|:--|:--|:--|:--|:--
'.'|点标记|'1'|下花三角标记|'h'|竖六边形标记
','|像素点标记(极小)|'2'|上花三角标记|'H'|横六边形标记
'o'|实心圈标记|'3'|左花三角标记|'+'|十字标记
'v'|倒三角标记|'4'|右花三角标记|'x'|x标记
'^'|上三角标记|'s'|实心方形标记|'D'|棱形标记
'>'|右三角标记|'p'|实心五角标记|'d'|廋棱形标记
'<'|左三角标记|'*'|星型标记|'\|'|竖线标记

![matplotlib5](/img/archive_img/matplotlib5.png)

下面遍历一次所有标记符号的样式
``` python
import matplotlib.pyplot as plt 
import numpy as np 
  
def main():
    color = 'bgrcmyk'
    line = ['-','--','-.',':']
    markers = '.,ov^><1234sp*hH+xDd|_'
    for i in range(len(markers)): 
        format_string = '{}{}{}'.format(color[i%len(color)], line[i%len(line)], markers[i])
        print("y -> format_string: {:>2d} -> {:4s} ".format(i+1,format_string) \
            if i%2 == 0 else "{:>5d} -> {} \n".format(i+1,format_string), end='')
        plt.plot(np.arange(len(markers)), np.full(len(markers),i+1), format_string)
    plt.axis([0,len(markers),0,len(markers)+1])
    plt.show()
 
if __name__ == "__main__":
    main()
 
""" out  # 无线条和白色线没有入队 因为看不到啊
y -> format_string:  1 -> b-.      2 -> g--,
y -> format_string:  3 -> r-.o     4 -> c:v
y -> format_string:  5 -> m-^      6 -> y-->
y -> format_string:  7 -> k-.<     8 -> b:1
y -> format_string:  9 -> g-2     10 -> r--3
y -> format_string: 11 -> c-.4    12 -> m:s
y -> format_string: 13 -> y-p     14 -> k--*
y -> format_string: 15 -> b-.h    16 -> g:H
y -> format_string: 17 -> r-+     18 -> c--x
y -> format_string: 19 -> m-.D    20 -> y:d
y -> format_string: 21 -> k-|     22 -> b--_
"""
```
 
![matplotlib6](/img/archive_img/matplotlib6.png)


*** 
## pyplot的中文显示  
#### 第一种方法  
pyplot并不默认支持中文显示, 需要rcParams修改字体实现
``` python
import matplotlib
import matplotlib.pyplot as plt 
 
if __name__ == "__main__":
    matplotlib.rcParams['font.family'] = 'SimHei'
    plt.plot([3,1,4,5,2])
    plt.ylabel("纵轴")
    plt.show()
```
![matplotlib7](/img/archive_img/matplotlib7.png)

rcParams的属性 

属性|说明 
:--|--
"font.family"|用于显示字体的名字
"font.style"|字体风格, 正常"normal" 或 斜体 "italic"
"font.size"|字体大小, 整数字号或"large"、"x-small"

目前只有中文黑体和楷体可以用 稍后研究  

中文字体|说明 
:--|:--
"SimHei"|中文黑体
"Kaiti"|中文楷体
"LiSu"|中文隶书
"FangSong"|中文仿宋
"YouYuan"|中文幼圆
"STSong"|华文宋体

``` python
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib 
 
def main():
    matplotlib.rcParams['font.family'] = "Kaiti"
    matplotlib.rcParams['font.size'] = 10
 
    a = np.arange(0.0, 5.0, 0.02)
 
    plt.xlabel("横轴：时间")
    plt.ylabel("纵轴：振幅")
    plt.plot(a, np.cos(2*np.pi*a), "r--")
    plt.show()
 
if __name__ == "__main__":
    main()
```

![matplotlib8](/img/archive_img/matplotlib8.png)

#### 第二种方法 推荐 
在有中文输出的地方, 增加一个属性: fontproperties  
``` python
import numpy as np 
import matplotlib.pyplot as plt 
 
def main():
    a = np.arange(0.0, 5.0, 0.02)
 
    plt.xlabel("横轴：时间", fontproperties="Kaiti", fontsize = 14)
    plt.ylabel("纵轴：振幅", fontproperties="SimHei", fontsize = 11)
    plt.plot(a, np.cos(2*np.pi*a), "r") # ??? 
    plt.show()
 
if __name__ == "__main__":
    main()
```
![matplotlib9](/img/archive_img/matplotlib9.png)

***
## pyplot的文本显示函数

函数|说明 
:--|:--
plt.xlabel()|对X轴增加文本标签
plt.ylabel()|对Y轴增加文本标签
plt.title()|对圆形整体增加文本标签
plt.text()|在任意位置增加文本
plt.annotate()|在图形中增加带箭头的注释
plt.grid(True)|图层显示网格

plt.annotate函数参数  
plt.annotate(s, xy= arrow_crd, xytext=text_crd, arrowprops=dict)
  * s : 表示要注解的字符串
  * xy : 箭头所在的位置
  * xytext ： 文本显示的位置
  * arrowprops : 字典 定义了整个箭头的属性

``` python
import numpy as np 
import matplotlib.pyplot as plt 
 
def main():
    a = np.arange(0.0, 5.0, 0.02)
    plt.plot(a, np.cos(2*np.pi*a), 'r--')
 
    plt.xlabel("横轴：时间", fontproperties="SimHei", fontsize=13, color="blue")
    plt.ylabel("纵轴：振幅", fontproperties="SimHei", fontsize=13)
    plt.title(r"正弦波实例 $y=cos(2\pi x)$",fontproperties="SimHei", fontsize = 15 )
    plt.text(4, 1, r"$\mu=100$", fontsize = 13)
     
    plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor="black", shrink=0.1, width=2))
 
    plt.axis([-1, 6, -2, 2 ])
    plt.grid(True)
    plt.show()
 
if __name__ == "__main__":
    main()
```

![matplotlib10](/img/archive_img/matplotlib10.png)

***
## pyplot的子绘图区域
#### 使用函数 plt.subplot21grid()
plt.subplot2grid(GridSpec, CurSpec, colspan=1, rowspan=1)
  * 理念: 设定网格, 选中网格, 确定选中行列区域数量,  编号从0开始
  * GridSpec : type tuple 把图层分为几行几列
  * CurSpec : type tuple 选择第几个位置 
  * colspan : 横向占用几个区域
  * rowspan : 纵向占用几个区域

``` python 
import numpy as np 
import matplotlib.pyplot as plt 
 
def main():
    a = np.arange(0.0, 5.0, 0.02)
 
    # (3,3) 绘图区域分为 3*3 共9个区域
    plt.subplot2grid((3,3), (0,0), colspan=3)   # (0,0) 选择第0行第0列 colspan 横向占3个区域 就是第一行都是这个图
    plt.plot(a, np.cos(2*np.pi*a), 'r--')       # 红色虚线
 
    plt.subplot2grid((3,3), (1,0), colspan=2)   # (1,0) 选择第1行第0列 colspan 横向占2个区域
    plt.plot(a, np.cos(2*np.pi*a), 'b-.')       # 蓝色虚线
 
    plt.subplot2grid((3,3), (1,2), rowspan=2)   # (1,2) 选择第1行第2列 rowspan 纵向占2个区域
    plt.plot(a, np.cos(2*np.pi*a), 'g' )        # 绿色实线
 
    plt.subplot2grid((3,3), (2,0))              # (2,0) 选择第2行第0列 后面不再填参数默认为1 占一个区域
    plt.plot(a, np.cos(2*np.pi*a),  'k' )       # 黑色实线
 
    plt.subplot2grid((3,3), (2,1))              # (2,1) 选择第2行第1列
    plt.plot(a, np.cos(2*np.pi*a), 'm' )        # 洋红色实线
 
    plt.show()
 
if __name__ == "__main__":
    main()
```

![matplotlib11](/img/archive_img/matplotlib11.png)

#### 使用 gridspec.GridSpec类 效果同上图
``` python 
import matplotlib.gridspec as gridspec 
import matplotlib.pyplot as plt
import numpy as np
  
def main():
    a = np.arange(0.0, 5.0, 0.02)
 
    # 将图层分成3*3的子区域
    gs = gridspec.GridSpec(3,3)
    # 使用gs切片选择绘图区域
    plt.subplot(gs[0,:])
    plt.plot(a, np.cos(2*np.pi*a), 'r--')
 
    plt.subplot(gs[1,:-1])
    plt.plot(a, np.cos(2*np.pi*a), 'b-.')
 
    plt.subplot(gs[1:,-1])
    plt.plot(a, np.cos(2*np.pi*a), 'g' ) 
 
    plt.subplot(gs[2,0])
    plt.plot(a, np.cos(2*np.pi*a),  'k' )
 
    plt.subplot(gs[2,1])
    plt.plot(a, np.cos(2*np.pi*a), 'm' )
 
    plt.show()
 
if __name__ == "__main__":
    main()
```

*** 
## pyplot常用基础图表函数

函数|说明| 
:--|:--|
plt.plot(x, y, fmt, ...)|绘制一个坐标图
plt.boxplot(data, notch, position)|绘制一个箱形图
plt.bar(left, height, width, bottom)|绘制一个条形图
plt.barh(width, bottom, left, height)|绘制一个横向条形图
plt.polar(theta, r) | 绘制极坐标图(这是啥)
plt.pie(data,  explode)|绘制饼图
plt.psd(x, NFFT=256, pad_to, Fs) | 绘制功率谱密度图
plt.specgram(x, NFFT=256, pad_to, Fs)|绘制谱图
plt.eohere(x, y, NFFT=256, Fs) | 绘制X-Y相关性图
plt.scatter(x, y) | 绘制散点图, 其中 x和y长度相同
plt.step(x, y, where) | 绘制步阶图
plt.hist(x, bins, normed) | 绘制直方图
plt.contour(X, Y, Z, N) | 绘制等值图
plt.vlines() | 绘制垂直图
plt.stem(x, y, linefmt, markerfmt)|绘制火柴图
plt.plot_date()|绘制数据日期

*** 
### 绘制饼图 

<details>
  <summary> 饼图代码 </summary>

``` python
import matplotlib.pyplot as plt 
 
def main():
    labels = "Frogs", "Hogs", "Dogs", "Logs"
    sizes  = [15, 30, 45, 10]
    explode= (0, 0.1, 0, 0)
 
    plt.pie(sizes, explode = explode, labels = labels,\
        autopct = "%1.1f%%", shadow = False, startangle = 90)
    plt.show() 
 
if __name__ == "__main__":
    main()
```

</details>  

![matplotlib12](/img/archive_img/matplotlib12.png)

***
### 绘制直方图 

<details>
  <summary> 直方图代码 </summary>

plt.hist(array, bin, 后面不知道)
* array : 直方图数据 
* bin : 直方的个数
* normed : 
    * 等于1时 将每一个直方中出现元素的个数规划为出现的概率 ？？？？？
    * 如果等于0 纵坐标就是直方区域中间出现的元素个数   ？？？？？


``` python
import numpy as np 
import matplotlib.pyplot as plt 
 
def main():
    np.random.seed(233)
    mu, sigma = 100, 20 # 均值和标准差
    a = np.random.normal(mu, sigma, size = 100)
 
    plt.hist(a, 40, normed = 0, histtype = "stepfilled", facecolor = "b", alpha = 0.75)
    plt.title('Histogram')
 
    plt.show()
 
if __name__ == "__main__":
    main()
```

</details>  

![matplotlib13](/img/archive_img/matplotlib13.png)

***
### 绘制极坐标图

<details>
  <summary> 极坐标图代码 </summary>

``` python
import numpy as np 
import matplotlib.pyplot as plt 
 
def main():
    N = 30
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
 
    ax = plt.subplot(111, projection = 'polar')
    bars = ax.bar(theta, radii, width = width, bottom = 0.0)
 
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.viridis(r / 10.))
        bar.set_alpha(0.5)
     
    plt.show()
 
if __name__ == "__main__":
    main()
```

</details>  
 
![matplotlib14](/img/archive_img/matplotlib14.png)

***
### 绘制引力波
> 摘自百度  
>在物理学中，引力波是指时空弯曲中的涟漪，通过波的形式从辐射源向外传播，这种波以引力辐射的形式传输能量。在1916年，爱因斯坦基于广义相对论预言了引力波的存在。引力波的存在是广义相对论洛伦兹不变性的结果，因为它引入了相互作用的传播速度有限的概念。相比之下，引力波不能够存在于牛顿的经典引力理论当中，因为牛顿的经典理论假设物质的相互作用传播是速度无限的。 


<details>
  <summary> 引力波代码 </summary>

两个wav文件是在 [python123.io](https://python123.io/dv/grawave.html) 下载的

``` python
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io import wavfile 
  
def main():
    """
    这是啥 
    """
    # wavfile读取速率与数据
    rate_h, hstrain = wavfile.read(r'H1_Strain.wav', 'rb')
    rate_l, lstrain = wavfile.read(r'L1_Strain.wav', 'rb')
    # reftime, ref_H1 = np.genfromtxt("wf_template.txt").transpose  # 模版用不了
  
    htime_interval = 1/rate_h
    ltime_interval = 1/rate_l
  
    htime_len = hstrain.shape[0]/rate_h
    htime = np.arange(-htime_len/2, htime_len/2, htime_interval)
    ltime_len = lstrain.shape[0]/rate_l
    ltime = np.arange(-ltime_len/2, ltime_len/2, ltime_interval)
  
    fig = plt.figure(figsize=(12, 6))
  
    plth = fig.add_subplot(211)
    plth.plot(htime, hstrain)
    plth.set_xlabel("Time (seconds)")
    plth.set_ylabel( "H1 Strain")
    plth.set_title("H1 Strain")
 
    plth = fig.add_subplot(212)
    plth.plot(ltime, lstrain, )
    plth.set_xlabel("Time (seconds)")
    plth.set_ylabel("L1 Strain")
    plth.set_title("L1 Strain")
  
    fig.tight_layout()
    plt.show()
    plt.close(fig)
  
if __name__ == "__main__":
    main()
```

</details>  
  

![引力波](/img/archive_img/matplotlib_grawave.png)
