---
title: 芯片问题
date: 2019-12-11 11:12:58 
tags:
- 算法
- python
categories: 算法
cover: /img/chip_problem.png
---
测试台可以放两块芯片 互相进行测试
测试报告只有 "好" or "坏"
* 好芯片的报告一定是正确的
* 坏芯片的报告是不确定的

#### 问题：
n片芯片，其中好芯片至少比坏芯片多1片。  
设计一种测试方法，通过测试从n片芯片中挑出一片好芯片  

*** 
测试报告分析:
 

|  A报告  |  B报告  |      结论       |
| :-----: | :-----: | :-------------: |
| B是好的 | A是好的 | A,B都好，或都坏 |
| B是好的 | A是坏的 | 至少一片是坏的  |
| B是坏的 | A是好的 | 至少一片是坏的  |
| B是坏的 | A是坏的 | 至少一片是坏的  |
 
 
*** 

问题： 给定芯片A，判定A的好坏  
方法： 用其他n-1片芯片对A测试。
根据题意得知 好芯片比坏芯片至少多1
####  假设1： n是奇数
 
n=7: 好芯片数 >= 4 
* A好，6个报告中至少有3个报告 "好"
* A坏，6个报告中至少有4个报告 "坏"

当n为奇数时：
* 好芯片数 >= (n+1)/2
* A好，至少有(n-1)/2个报告 "好"
* A坏，至少有(n+1)/2个报告 "坏"

结论：
* 至少一半报 "好"， A是好芯片
* 超过一半报 "坏"， A是坏芯片

####  假设2: n是偶数
n=8: 好芯片数 >= 5 
* A好，7个报告中至少有4个报告 "好"
* A坏，7个报告中至少有5个报告 "坏"

当n为奇数时：
* 好芯片数 >= n/2+1
* A好，至少有 n/2 个报告 "好"
* A坏，至少有 n/2+1 个报告 "坏"

结论：
* 至少一半报 "好"， A是好芯片
* 超过一半报 "坏"， A是坏芯片

*** 
## 蛮力算法
#### 测试方法:
任取1片芯片测试，如果是好芯片，测试结束；如果是坏芯片，抛弃，再从剩下芯片任取1片测试，直到得到好芯片。
#### 时间估计 O(n²)

*** 
## 分治算法
假设n为偶数，将n片芯片两两一组做测试淘汰，剩下芯片构成子问题，进入下一轮分组淘汰。

#### 淘汰规则
* "好，好" -> 任意留一片,进入下轮
* 其他情况 -> 全部抛弃

#### 截止条件 n <= 3
3片芯片，1次测试可得知好芯片。
1或2片芯片，不需测试 都是都是好芯片
仅存3片芯片时，至少有2片是好的 任意取两片测试
* 两个都报告好，那就是真的都是好芯片
* 有一个报告坏，说明坏芯片在测试台上，没有上台的那片直接输出答案

#### 分治算法正确性
命题1：当n是偶数时，在上述淘汰规则下，经过一轮淘汰，剩下好芯片毕坏芯片至少多1片。
证：设
A,B都是好芯片i组
A与B一好一坏j组  
A与B都坏的k组  
淘汰后好芯片至少i片坏芯片之多k片
* 2i + 2j + 2k = n  # 初始芯片总数
* 2i + j > 2k +j  # 左侧是原来好芯片数，右侧原来坏芯片数 
* i > k #  

淘汰以后 好芯片依旧比坏芯片多 

命题2：当n为奇数时 可能会出问题
输入："好 好 好 好 坏 坏 坏"
分组: ["好" "好"] ["好" "好"] ["坏" "坏"] "坏"
淘汰后: "好" "好" "坏" "坏"
处理方法： 当n为奇数时 增加一轮对轮空的芯片单独测试，
如果是好芯片，算法结束；
如果是坏芯片，淘汰坏芯片，保持好芯片比坏芯片至少多一片条件

#### 算法复杂度 O(n)
<details>
  <summary> python代码 </summary>

```  python
import random
 
# 是否使用测试用例
debug_example = False
# type example: [[int, bool], [int, bool] ... ]
example =  [ [0, False], [1, True], [2, False], [3, False], [4, True], [5, True] ]
 
# 随机创建实例个数范围
rand_min = 50
rand_max = 100
 
class chip():
    def __init__(self, number,quality):
        self.number = number
        self.quality = quality
    
    def test_target(self, target):
        # type target : chip
        # rtype ： bool
        # 接收一个芯片实例形参 判断该芯片好坏 返回bool
        # 如果本实例是好芯片 不会说谎 直接报告目标芯片的quality
        # 如果本实例不是好芯片 报告就有不确定性 返回一个随机值
        if self.quality:
            return target.quality
        else:
            return random.choice((True,False))
 
def create_chips():
    # rtype : list[chip,chip,...]
    # 随机创建实例 随机好坏
    # 最后补正好芯片比坏芯片多条件
    # 随机选取1或2个坏芯片改成好的 使得好芯片比坏芯片多
    chips = []
    quality_count = 0
    badnums = []
    for x in range(random.randint(rand_min,rand_max)):
        if random.choice((True,False)):
            chips.append(chip(number = x, quality = True))
            quality_count += 1
        else:
            chips.append(chip(number = x, quality = False))
            badnums.append(x)
    while quality_count <= len(chips)/2:
        for _ in range(random.choice((1,2))):
            num = badnums.pop(random.randint(0,len(badnums)-1))
            chips[num].quality = True
            quality_count += 1
    return chips
 
def test(A,B):
    # type A: chip
    # type B: chip
    # rtype : bool
    return A.test_target(B) and B.test_target(A)
 
def create_test_chips():
    # rtype : list[chip, chip...]
    chips = []
    for i in example:
        chips.append(chip(number = i[0], quality = i[1]))
    return chips    
 
def main():
    # rtype : chip
    if debug_example:
        chips = create_test_chips()
    else:
        chips = create_chips()
    while len(chips) > 3:
        # 当总量为奇数时 对最后一个元素单独判断 
        # 循环遍历前面的元素 与最后一个元素测试 得到最后一片芯片的quality 
        if len(chips)%2 != 0:    
            count = 0
            for i in chips[:-1]:
                if i.test_target(chips[-1]):
                    count += 1
            if count >= len(chips)//2: # 此时已经发现最后一片是好芯片
                return chips[-1]
            else:
                chips.pop()
        else:   # 如果不是奇数 进入分组淘汰模式
            surplus = []
            for i in range(len(chips)//2):
                # 两两一组互相测试 都报告好芯片 就随机选一个进入下一轮
                if test( chips[i*2], chips[i*2+1] ):
                    surplus.append( chips[ i*2 + random.choice((0, 1))] )
            chips = surplus   
    
    if len(chips) <= 2:
        return chips[0]
    elif len(chips) == 3:
        if test(chips[0],chips[1]):
            return chips[0]
        else:
            return chips[2]
    else:
        print("Error!")
        return        
 
if __name__ == "__main__":
    target = main()
    print("target:\nnumber {}\nquality {}".format( target.number, target.quality))
```  
</details>  





