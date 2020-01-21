---
title: 制作chrome浏览器新标签页
date: 2020-1-20 14:01:43
tags: 
- chrome 
cover: img/chrome_new_tab.jpg
---

## chrome扩展程序是什么
> 摘自百度
> 拓展就是利用浏览器提供给你的功能，通过自己搭配来实现一些功能组合，通常利用JavaScript这样的脚本语言来完成，只要调用浏览器提供的接口即可。
 
从chrome网上应用商店下载的扩展 都是.crx文件 安装完自动删除了 离线只能从其他地方下载 
参考了离线安装.crx的教程 
把.crx 替换成 .zip 居然能打开 
里面就是一个html网页 有配置信息 静态资源.
 
那么可以总结为 .crx文件其实这就是一个zip压缩包？
既然有这样的规则 我尝试了下制作测试扩展

***
## 如何制作
 
我们先来看个最低配置例子  
![](/img/archive_img/chrome_new_tab2.png)
然后开启开发者模式 加载已解压的扩展程序 选择上面写代码的文件夹
最后得到我们的cocoa 1 扩展 
![](/img/archive_img/chrome_new_tab3.png)

打开新标签 熟悉的hello world! 来了
![](/img/archive_img/chrome_new_tab1.png)

有了这个知识 就能做更多自定义的功能了   
喜欢什么加什么 不必受限于大众化的首页  

***
## 使用过的新标签扩展
* Infinity 
   * 扩展界面不错 就是图标太大了 我希望图标可以放在最底下一排 可是没得设置
* Infinite 
   * 太简单 就一个壁纸和搜索框 啥都没了 自定义也少
* Momentum 
   * 更简单
* My Tab
   * 界面不错 中间搜索框 最下面一组网站的小图标 可是为什么不能修改图标指向的网站  
   * 不能离线使用 本质其实是指向其他网页 既然用户要使用 直接主页设置为那个网页不就完了 要扩展何用。

最后 我发现了Infinity Pro 当我看到自定义布局时 我就知道这是我想要的标签页
![](/img/archive_img/chrome_new_tab4.png)

## 魔改
[infinity安装包](https://github.com/Hotobun/chrome_infinity)  
官方的配置已经够好了 但是还有所欠缺 每个人胃口不同。
* 修改了图标位置 固定在窗口最下方 
* 隐藏了网站图标的文字 看头像认人的时代 还是不喜欢文字占地方
* 隐藏了搜索框 鼠标移动到搜索框区域 自动打开

缺点: 当鼠标点击在页面外部时 再次移动鼠标到搜索框 焦点不会定位到input标签 优先级不够?

<details>
  <summary> search_click.js </summary>
  
```
// 隐藏搜索框 
// 鼠标移动到搜索框区域再取消隐藏 
// 5秒内无键盘操作 隐藏搜索框
// 若搜索框已开启 移动鼠标会重置计时器
 
window.onload = function () {
    var search_flag_id = window.setInterval(function () {
        var search_father = document.getElementsByClassName("gH3horrwzk1vWQb_tjFZ_")[0];
        var search_div = document.getElementsByClassName("j6WjrWzBT0VSJtD8yafTe")[0]; //获取到div的id
        var search_input = document.getElementsByClassName("DmH9A0dYKnyClIjOJ5xWt")[0];
        if (search_father != undefined && search_div != undefined && search_input != undefined) {
            var keyboard_count = 0
            var keyboard_timeout = 6
            search_flag = false
            clearInterval(search_flag_id);
            // 循环已停止 均已获得标签元素
            // 设置搜索框焦点
            search_input.focus()
            // 一开始时 先隐藏掉搜索框 
            search_div.style.display = "none";
            // 为上级div加上鼠标监控  
            search_father.onmouseover = function () {
                search_div.style.display = "block";
                search_input.focus()
                keyboard_count = 0
            }
 
            window.setInterval(input_style_status, 1000)

            function input_style_status() {
                keyboard_count++;
                if (keyboard_count >= keyboard_timeout) {
                    search_div.style.display = "none";
                }
            }
            // 监听键盘
            document.onkeydown = function () {
                keyboard_count = 0;
            }
            // 监听鼠标
            document.onmousemove = function (event) {
                var x1 = event.clientX;
                var y1 = event.clientY;
                if (search_div.style.display == "block") {
                    if (x != x1 || y != y1) {
                        keyboard_count = 0;
                    }
                }
                x = x1;
                y = y1;
            };
        }
    }, 3)
}
```

</details>  

最后两幅效果图
![](/img/archive_img/chrome_new_tab5.png)
![](/img/archive_img/chrome_new_tab6.png)