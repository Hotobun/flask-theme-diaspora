---
title: Matplotlib裁剪圆形图片
date: 2020-1-27 00:01:31
tags: 
- Python
- Matplotlib
categories:
cover: /img/matplotlib_circular_image.jpg
---
 
官网抄的  
注意PNG图片的头信息 有的PNG图片虽然能打开看   
但是如果信息已经丢失的 这里打不开  
比如.PNG文件 直接改成 .jpg 再改回来 .PNG 信息已丢失  
解决  
* 找个ps软件放上去 导出为PNG 大概可以 
* 或者简单除暴 直接用.JPG
 
 
``` python
import os
 
def main():
    cwd = os.getcwd()
    filename = input("图片文件名或图片完整路径: ")
    if filename:
        if os.path.isfile(os.path.join(cwd, filename)):
            file_path = os.path.join(cwd, filename)
        elif os.path.isfile(filename):
            file_path = filename
        else:
            print("该路径不是一个文件 {}".format(filename))
            print("该路径不是一个文件 {}".format(os.path.join(cwd, filename)))
            print("未找到图片 告辞!")
            return 
    else:
        return main() 
 
    with cbook.get_sample_data(file_path) as image_file:
        image = plt.imread(image_file)
 
    fig, ax = plt.subplots()
    im = ax.imshow(image)
    imsize = im.get_size() # 返回 (高, 长) 跟平时的长*高 反过来的！ 
    print("图片尺寸 ", imsize[::-1])
  
    # center 裁剪的圆心位置 这里默认图片中心
    # min_r  圆形图片半径 取长高最小值除2 再大会有切片 不能构成圆形
    center = (imsize[1]//2, imsize[0]//2)
    min_r = min(imsize)//2
  
    patch = patches.Circle(center, radius=min_r, transform=ax.transData)
    im.set_clip_path(patch)
 
    ax.axis('off')
    print("圆心坐标:{} 半径:{}\n".format(center, min_r))
    if save_name:
        plt.savefig(save_name)
    plt.show()
 
if __name__ == "__main__":
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        import matplotlib.cbook as cbook  
    except ModuleNotFoundError as e:
        print("ModuleNotFoundError 请安装绘图库 Matplotlib ")
        print("    $ pip install matplotlib")
        exit()
    save_name = ''
    main()
```

![](/img/archive_img/matplotlib_circular_image.png)