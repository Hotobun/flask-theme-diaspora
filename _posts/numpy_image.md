---
title: Numpy图像处理
date: 2020-1-06 18:01:33
tags: 
- python
- numpy
- pillow
categories:
cover: /img/numpy_image.jpg
---

## 图像的RGB色彩模式  
RGB三个颜色捅到的变化和叠加得到各种颜色，其中：  
* R红色, 取值范围, 0-255  
* G绿色, 取值范围, 0-255  
* B蓝色, 取值范围, 0-255  
RGB形成的颜色包括了人类视力所能感知的所有颜色。

这里有1张图像  
图像可以平铺成xy轴形成的像素阵列  
每一个图像都是由三个字节作为一个元素形成的二维矩阵  
![](/img/archive_img/numpy_miku.jpg)

这里需要用到PIL库
``` python
>>> import numpy as np
>>> from PIL import Image
>>> miku = np.array(Image.open("miku.jpg"))
>>> print(miku.shape, miku.dtype)
(1135, 1000, 3) uint8
```

打开图像发现 这张图片是一个三维数组
分别是高度、宽度、像素rgb值

既然图片是可以用数据来表示  
那么我们修改它的值 是不是就等于可以修改图片？
于是 我们再弄一张图片
![](/img/archive_img/numpy_hat.png)
```python
>>> hat = np.array(Image.open("hat.png"))
>>> hat
array([[[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ...,        # 此处省略非常多行 无法直观查看
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]], dtype=uint8)
 
# 可以看到这张图片非常多rgb值全为0的像素   
# 这些像素其实是空白的 什么都没有 但是在矩阵中间就有我们要的帽子图片数据
 
>>> print("图像高度 = {}\n图像宽度 = {}".format(len(hat),len(hat[0])))
图像高度 = 167
图像宽度 = 515
  
# 下面来遍历一次hat的像素 
# 如果是像素不空 就是帽子的数据 用帽子覆盖原图的数据
# png是4色rgb jpg是三色 这里就舍弃第四色了 因为尝试了三色最后补0 是纯白色的
>>> for x in range(hat.shape[0]):
        for y in range(hat.shape[1]):
            if sum(hat[x][y]) != 0:      
                
                miku[x][y] = hat[x][y][:3]  
 
# 保存新图像	
>>> new_img = Image.fromarray(miku.astype('uint8'))
>>> new_img.save("new_miku.jpg")

```

合成后的图片  
为什么位置这么好？ 因为我在ps上先摆好位置了 前面用空白填充占位  
技术渣 一看就知道合成的 边缘无解
![](/img/archive_img/numpy_new_miku.jpg)


***
## 图像变换
有了上面知识之后 我们可以对图像做更多的处理
``` python
from PIL import Image
import numpy as np 
 
def func1():
    new = [255,255,255] - np.array(miku_img)
    Image.fromarray(new.astype('uint8')).save("miku1.jpg")
 
def func2():
    miku = np.array(miku_img.convert("L"))
    new = 255 - miku
    Image.fromarray(new.astype('uint8')).save("miku2.jpg")
 
def func3():
    new = (100/255) * np.array(miku_img) + 150
    Image.fromarray(new.astype('uint8')).save("miku3.jpg")
 
def main():
    func1()
    func2()
    func3() 
 
if __name__ == "__main__":
    miku_img = Image.open("miku.jpg")
    main()
```

不知道叫什么图 直接放出来做对比吧 分别对应func1、func2、func3
![](/img/archive_img/miku1.jpg)
![](/img/archive_img/miku2.jpg)
![](/img/archive_img/miku3.jpg)