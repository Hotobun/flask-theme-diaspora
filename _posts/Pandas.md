---
title: Pandas
date: 2020-1-07 18:01:39
tags: 
- pandas
- python
categories:
cover: /img/pandas.png
---

## 什么是Pandas
#### Pandas是Python第三方库, 提供高性能易用数据类型和分析工具。  
1. 提供了便于操作数据的数据类型。
2. 提供很多分析函数与分析工具, 使得数据分析变得非常容易操作

Pandas基于NumPy实现, 常与NumPy和Matplotlib一同使用。
引用Pandas  
``` python
import pandas as pd
```

<details>
  <summary> pandas基础使用 </summary>

``` python
>>> import pandas as pd
>>> pd.Series(range(20))
0      0
1      1
2      2
3      3
4      4
5      5
6      6
7      7
8      8
9      9
10    10
11    11
12    12
13    13
14    14
15    15
16    16
17    17
18    18
19    19
dtype: int64
```

</details>  
  
<details>
  <summary> 计算前N项累加和 </summary>

``` python
>>> pd.Series(range(20)).cumsum()
0       0
1       1
2       3
3       6
4      10
5      15
6      21
7      28
8      36
9      45
10     55
11     66
12     78
13     91
14    105
15    120
16    136
17    153
18    171
19    190
dtype: int64
```

</details>  
  
  
#### Pandas的理解
Pandas主要提供两个数据类型: Series, DataFrame
这两个数据类型构成Pandas的基础
* 基于上述数据类型的各类操作
* 基本操作、运算操作、特征类操作、关联类操作

#### 与NumPy对比
NumPy|Pandas
:--|:--
基础数据类型|扩展数据类型
关注数据的结构表达|关注数据的应用表达
维度:数据之间的关系|数据与索引之间关系


## Pandas的Series
Series类型由一组数据及与之相关的数据索引组成。  
```
  索引  --->  数据  
index_0 ---> data_a  
index_1 ---> data_b  
index_2 ---> data_c  
index_3 ---> data_d  
```

<details>
  <summary> 举个栗子 </summary>

``` python
>>> a = pd.Series([9,8,7,6])
>>> a
0    9      # 9876 为数据的值
1    8      # 0123 为数据索引
2    7
3    6
dtype: int64  # 基于NumPy 所有数据类型沿用了NumPy
```

</details>  

<details>
  <summary> 自定义索引 </summary>

``` python
>>> b = pd.Series([9,8,7,6,5,4,3], index = [x for x in "abcdefg"])
>>> b
a    9
b    8
c    7
d    6
e    5
f    4
g    3
dtype: int64
```

</details>  


Series类型可以由下如下类型创建
* Python列表, index与列表元素个数一致。
* 标量值, index表达Series类型的尺寸。
* Python字典, 键值对中的key 是索引, index从字典中进行选择操作。
* ndarray, 索引和数据都可以通过ndarray类型创建
* 其他函数 range() 等...

<details>
  <summary> 从标量值创建Series </summary>

``` python
>>> pd.Series(233 , index =  [x for x in "abcd"])
a    233
b    233    # 此处index不可省略 生成数据个数为 len(index)
c    233
d    233
dtype: int64
```

</details>  
  
  
<details>
  <summary> 从字典类型创建Series </summary>

``` python
# 普通创建 
>>> pd.Series({'a':11, 'b':22, 'c':33})
a    11
b    22     # 键值对关系变为 索引 -> 数据 
c    33
dtype: int64
 
 
# 自定义index 
>>> pd.Series({'a':11, 'b':22, 'c':33}, index = [x for x in "cabd"])
c    33.0
a    11.0   # index指定Series的结构
b    22.0   # 按照结构顺序从字典中取值
d     NaN   # NaN表示python中的None
dtype: float64

```

</details>  
  

<details>
  <summary> 从ndarray类型创建 </summary>

``` python
>>> pd.Series(np.arange(25,30))
0    25
1    26
2    27
3    28
4    29
dtype: int32
 
# 自定义index 
>>> pd.Series(np.arange(25,30), index= np.arange(9,4,-1))
9    25
8    26
7    27
6    28
5    29
dtype: int32
```
  
</details>  
  
***
## Series类型的基本操作
* Series类型包括index和values两部分。
* Series类型的操作类似Python字典类型。
* Series类型的操作类似ndarray类型。
  * 索引方法相同, 采用切片方式。 
  * NumPy中运算和操作可用于Series类型。
  * 可以通过自定义索引的列表进行切片。 
  * 可以通过自动索引进行切片, 如果存在自定义索引, 则一同被切片。 

<details>
  <summary> 举个栗子 </summary>

``` python
>>> a = pd.Series([9,8,7,6], index = [x for x in "abcd"])
>>> a
a    9
b    8
c    7
d    6
dtype: int64
 
>>> a.index
Index(['a', 'b', 'c', 'd'], dtype='object')
 
>>> a.values
array([9, 8, 7, 6], dtype=int64)
  
>>> type(a)
<class 'pandas.core.series.Series'>
 
>>> type(a.index)
<class 'pandas.core.indexes.base.Index'>
 
>>> type(a.values)
<class 'numpy.ndarray'>
```

</details>  
  
  
#### Series类型索引
* 自动索引和自定义索引是共存的
* 两套索引不可以混用

<details>
  <summary> 举个栗子 </summary>

``` python
>>> a
a    9
b    8
c    7
d    6
dtype: int64
 
>>> a['b']  # 使用自定义索引 和 自动索引下标 均可取值
8
 
>>> a[1]
8
 
>>> a[['c', 'd', 0]]    # 两天索引混用 得到一个Warning 
                        # 混合使用时 会当做自定义索引 系统会产生一个自定义索引 0
Warning (from warnings module):
  File "...\series.py", line 1155
    return self.loc[key]
FutureWarning: 
Passing list-likes to .loc or [] with any missing label will raise
KeyError in the future, you can use .reindex() as an alternative.
 
See the documentation here:
https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
#deprecate-loc-reindex-listlike
c    7.0
d    6.0
0    NaN    # 自定义索引没有 0 所以是NaN
dtype: float64
 
>>> a[['c', 'd', 'a']]
c    7
d    6
a    9
dtype: int64
 
>>> a   # 再次查看a 没有改变原Series 
a    9
b    8
c    7
d    6
dtype: int64
```

</details>  
  
<details>
  <summary> 举个栗子 </summary>

``` python
>>> a
a    9
b    8
c    7
d    6
dtype: int64
 
>>> a[3]    # 如果只取一个值 类型就是值本身 而不是Series
6
 
>>> a[:3]   # 切片后仍然是Series类型
a    9
b    8
c    7
dtype: int64
 
>>> a[a > a.median()]   # 把所有大于中位数的元素输出
a    9
b    8
dtype: int64
 
>>> np.exp(a)   # 
a    8103.083928
b    2980.957987
c    1096.633158
d     403.428793
dtype: float64
```

</details>  
  

#### Series的 in 操作与Python中的字典类似
`val in Series` 判断的是Series是否存在索引val 而不是值val

<details>
  <summary> Series in 栗子 </summary>

``` python
>>> a
a    9
b    8
c    7
d    6
dtype: int64
 
>>> 'c' in a
True
 
>>> 9 in a
False
 
>>> a.get("f", 100)
100
```

</details>  
  

#### Series类型对齐操作  
Series类型在运算忠会自动对其不同索引的数据  
两个Series类型相加时  
* 返回结果包含了两个Series对象的所有的并集   
* 只有索引相同才会进行运算 索引不同的不进行运算 返回NaN  
  
<details>    
  <summary> Series 对齐栗子 </summary>

``` python
>>> a = pd.Series([1,2,3], [x for x in "cde"])
>>> b = pd.Series([9,8,7,6], [x for x in "abcd"])

>>> a
c    1
d    2
e    3
dtype: int64
 
>>> b
a    9
b    8
c    7
d    6
dtype: int64
 
>>> a + b   # 有一个对象中没有值 就返回空
a    NaN
b    NaN
c    8.0
d    8.0
e    NaN
dtype: float64
```

</details>  
  
  
#### Series类型的name属性
Series对象和索引都可以有一个名字,  存储在属性.name中。 

<details>
  <summary> Series.name 栗子 </summary>

``` python
>>> a = pd.Series([1,2,3], [x for x in "cde"])
>>> a.name # None
>>> a.name = "我家的Series"
>>> a.index.name = "这是你家的索引"
 
>>> a
这是你家的索引
c    1
d    2
e    3
Name: 我家的Series, dtype: int64
```

</details>  
  
  
#### Series类型的修改
Series对象可以随时修改并立即生效  
可以同时为多个已存在的索引赋值  

<details>
  <summary> 举个栗子 </summary>

``` python
>>> a = pd.Series([1,2,3,4], [x for x in "abcd"])
>>> a
a    1
b    2
c    3
d    4
dtype: int64
 
>>> a["a"] = 11
>>> a
a    11
b     2
c     3
d     4
dtype: int64
 
>>> a['c','d'] = 99 
>>> a
a    11
b     2
c    99
d    99
dtype: int64
```

</details>  
  
  
*** 
## Pandas的DataFrame类型
DataFrame类型由共用相同索引的一组列组成。  
DateFrame是一个表格型的数据类型, 每列值类型可以不同。   
DateFrame既有行索引、也有列索引。  
DateFrame常用语表达二维数据，但也可以表达多维数据。
DateFrame类型可以由如下类型创建:
* 二维ndarray对象
* 由一维ndarray、列表、字典、元祖、或Series构成的字典
* Series类型
* 其他的DataFrame类型

<details>
  <summary> 从二维ndarray对象创建DataFrame </summary>

``` python
>>> d = pd.DataFrame(np.arange(10,20).reshape(2,5))
>>> d
    0   1   2   3   4   # 行索引
0  10  11  12  13  14
1  15  16  17  18  19
```

</details>  
    
  
<details>
  <summary> 自动补齐 </summary>

``` python
>>> dt = {
	"one":pd.Series([1,2,3], [x for x in "abc"]),
	"two":pd.Series([9,8,7,6], [x for x in "abcd"]),
	}

>>> d = pd.DataFrame(dt)
>>> d  
   one  two
a  1.0    9
b  2.0    8
c  3.0    7
d  NaN    6     # one 缺少d 自动补齐
  
    # 数据根据行列索引自动补齐
>>> pd.DataFrame(dt, index=[x for x in "bcd"], columns=["two", "three"])
   two three
b    8   NaN
c    7   NaN
d    6   NaN
```

</details>  
  
  
<details>
  <summary> 从列表类型的字典创建 </summary>

``` python
>>> dl = {"one":[1,2,3,4], "two":[9,8,7,6]}
>>> d = pd.DataFrame(dl, index = [x for x in "zxcv"])
>>> d
   one  two
z    1    9
x    2    8
c    3    7
v    4    6
```

</details>  
  
  
<details>
  <summary> DataFrame取下标 </summary>

``` python
# 首先我没有数据 先模拟出一组数据
>>> dl = {
	"城市":['北京',"上海","广州","深圳"],
	"环比":['1', '2', '3', '4'],
	"同比":['5', '6', '7', '8'],
	"定基":['9', '10', '11', '12']
	}
      
>>> d = pd.DataFrame(dl, index = ['c1', 'c2', 'c3', 'c4'])
>>> d
    城市 环比 同比  定基
c1  北京  1  5   9
c2  上海  2  6  10
c3  广州  3  7  11
c4  深圳  4  8  12
 
>>> d["环比"]
c1    1
c2    2
c3    3
c4    4
Name: 环比, dtype: object
 
>>> d["同比"]["c2"]
'6'
```

</details>  
  
  
*** 
## Pandas库的数据类型操作 
如何改变Series和DataFrame对象？
* 增加或重排 : 重新索引
* 删除 : drop

#### 重新索引
.reindex(index=None, columns=None, ...)  
能够改变或重排Series和DataFrame索引    
返回新对象 不改变原数据    
 
参数|说明 
:--|:--
index, columns | 新的行列自定义索引
fill_value | 重新索引中, 用于填充缺失位置的值
method | 填充方法, ffill当前值向前填充, bfill向后填充
limit | 最大填充量
copy | 默认True, 生成新的对象, False时, 新旧相等不复制




<details>
  <summary> reindex栗子 </summary>

``` python
# 拿前面的栗子
>>> d
    城市 环比 同比  定基
c1  北京  1  5   9
c2  上海  2  6  10
c3  广州  3  7  11
c4  深圳  4  8  12

# 注意 改索引是没有数据的
>>> d.reindex(index=[x for x in "abcd"])
    城市   环比   同比   定基
a  NaN  NaN  NaN  NaN
b  NaN  NaN  NaN  NaN
c  NaN  NaN  NaN  NaN
d  NaN  NaN  NaN  NaN

# 改变列索引的顺序
>>> d.reindex(index=['c1', 'c2', 'c3', 'c4'][::-1])
    城市 环比 同比  定基
c4  深圳  4  8  12
c3  广州  3  7  11
c2  上海  2  6  10
c1  北京  1  5   9
 
# 改变行索引顺序
>>> d.reindex(columns=["城市","定基","环比","同比"])
    城市  定基 环比 同比
c1  北京   9  1  5
c2  上海  10  2  6
c3  广州  11  3  7
c4  深圳  12  4  8


```

</details>  
  
  
<details>
  <summary> 增加一列数据 </summary>

``` python
>>> newd = d.columns.insert(4,"新增")
>>> newd
Index(['城市', '环比', '同比', '定基', '新增'], dtype='object')
  
>>> newd = d.reindex(columns=newd, fill_value = 200)
>>> newd
    城市 环比 同比  定基   新增
c1  北京  1  5   9  200
c2  上海  2  6  10  200
c3  广州  3  7  11  200
c4  深圳  4  8  12  200
```

</details>  
  
  
#### 索引类型
Series和DataFrame的索引是Index类型   
Index类型是不可变类型  
``` python 
>>> d.index
Index(['c1', 'c2', 'c3', 'c4'], dtype='object')
>>> d.columns
Index(['城市', '环比', '同比', '定基'], dtype='object')
>>> type(d.index)
<class 'pandas.core.indexes.base.Index'>
```

索引类型的常用方法

方法|说明 
:--|:--
.append(idx)| 连接另一个Index对象, 产生新的Index对象
.diff(idx) | 计算差集, 产生新的Index对象
.intersection(idx) | 计算交集
.union(idx) | 计算并集
.delete(loc) | 删除loc位置处的元素
.insert(loc, e) | 在loc位置增加一个元素 e 

<details>
  <summary> 举个栗子 </summary>

``` python
>>> ni = d.index.insert(4, "c5")
>>> nc = d.columns.delete(2)
>>> ni
Index(['c1', 'c2', 'c3', 'c4', 'c5'], dtype='object')
 
>>> nc
Index(['城市', '环比', '定基'], dtype='object')
 
>>> nd = d.reindex(index=ni, columns=nc)
>>> nd
     城市   环比   定基
c1   北京    1    9
c2   上海    2   10
c3   广州    3   11
c4   深圳    4   12
c5  NaN  NaN  NaN
 
 # 挖个坑
>>> nd = d.reindex(index=ni, columns=nc, method='bfill')
        ...
    raise ValueError("index must be monotonic increasing or decreasing")
ValueError: index must be monotonic increasing or decreasing

```

</details>  
  
  
#### 删除指定索引对象
.drop() 能够删除Series和DataFrame指定行或列
注意 返回的是新对象 函数不改变原数据

<details>
  <summary> 举个栗子 </summary>

``` python
>>> a = pd.Series([9,8,7,6],[x for x in "abcd"])
>>> a
a    9
b    8
c    7
d    6
dtype: int64
  
>>> a.drop(['b','c'])
a    9
d    6
dtype: int64

>>> d
    城市 环比 同比  定基
c1  北京  1  5   9
c2  上海  2  6  10
c3  广州  3  7  11
c4  深圳  4  8  12
 
>>> d.drop('c4')    # axis 默认为0 可以不指定
    城市 环比 同比  定基
c1  北京  1  5   9
c2  上海  2  6  10
c3  广州  3  7  11
 
>>> d.drop("环比",axis = 1) # axis = 1为操作列索引
    城市 同比  定基
c1  北京  5   9
c2  上海  6  10
c3  广州  7  11
c4  深圳  8  12
```

</details>  
  
  
***
## Pandas库的数据类型运算
#### 算术运算法则
* 算术运算根据行列索引, 补齐后运算, 默认产生浮点数。 
* 补齐时缺项填充 NaN (空 None)
* 二维和一维、一维和零维间为广播运算
* 采用 +-*/ 符号进行的二元运算产生新的对象
  
<details>
  <summary> 个数不同运算栗子 </summary>

``` python
>>> a = pd.DataFrame(np.arange(12).reshape(3,4))
>>> a
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
 
>>> b = pd.DataFrame(np.arange(20).reshape(4,5))
>>> b
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19

# 自动补齐 缺项填充NaN
>>> a + b
      0     1     2     3   4
0   0.0   2.0   4.0   6.0 NaN
1   9.0  11.0  13.0  15.0 NaN
2  18.0  20.0  22.0  24.0 NaN
3   NaN   NaN   NaN   NaN NaN
 
>>> a * b
      0     1      2      3   4
0   0.0   1.0    4.0    9.0 NaN
1  20.0  30.0   42.0   56.0 NaN
2  80.0  99.0  120.0  143.0 NaN
3   NaN   NaN    NaN    NaN NaN
```

</details>  
  

方法形式的算数运算
  
方法|说明 
:--:|:--:
.add(d, **argws) | 类型间加法运算, 可选参数
.sub(d, **argws) | 类型间减法运算, 可选参数
.mul(d, **argws) | 类型间乘法运算, 可选参数
.div(d, **argws) | 类型间除法运算, 可选参数

<details>
  <summary> 方法形式运算栗子 </summary>

``` python
>>> a
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
 
>>> b
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19
 
 # a跟b之间 元素缺少的部分 使用fill_value填充
>>> b.add(a, fill_value = 100)
       0      1      2      3      4
0    0.0    2.0    4.0    6.0  104.0
1    9.0   11.0   13.0   15.0  109.0
2   18.0   20.0   22.0   24.0  114.0
3  115.0  116.0  117.0  118.0  119.0
 
>>> a.mul(b, fill_value = 0)
      0     1      2      3    4
0   0.0   1.0    4.0    9.0  0.0
1  20.0  30.0   42.0   56.0  0.0
2  80.0  99.0  120.0  143.0  0.0
3   0.0   0.0    0.0    0.0  0.0
```

</details>  
  
  
<details>
  <summary> 不同维度之间的广播运算 </summary>

``` python
>>> b = pd.DataFrame(np.arange(20).reshape(4,5))
>>> b
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19
>>> c = pd.Series(np.arange(4))
 
>>> c
0    0
1    1
2    2
3    3
dtype: int32
 
 # c中的每一个元素都与10做减法 这样的操作叫广播 低维度元素或作用到高纬度的每一个元素
>>> c - 10
0   -10
1    -9
2    -8
3    -7
dtype: int32
 
 # b中的每一行 都与c进行运算
 # 二维和一维数据运算时 
 # 一维Series默认在轴1参与运算
>>> b - c
      0     1     2     3   4
0   0.0   0.0   0.0   0.0 NaN
1   5.0   5.0   5.0   5.0 NaN
2  10.0  10.0  10.0  10.0 NaN
3  15.0  15.0  15.0  15.0 NaN
 
 # 如果需要0轴运算 需要使用方法 + 参数axis = 0
>>> b.sub(c, axis = 0)
    0   1   2   3   4
0   0   1   2   3   4
1   4   5   6   7   8
2   8   9  10  11  12
3  12  13  14  15  16 

 # 0轴参与运算 
>>> b.sub(c, axis = 0)
    0   1   2   3   4
0   0   1   2   3   4
1   4   5   6   7   8
2   8   9  10  11  12
3  12  13  14  15  16
```

</details>  
  
  
#### 比较运算法则
比较运算之鞥呢比较相同索引的元素, 不进行补齐。  
二维和一维、一维和0维之间为广播运算。    
采用比较运算符号进行的二元运算产生布尔对象。  
* 相同纬度运算 要求尺寸一致。
* 不同维度, 广播运算, 默认在1轴

<details>
  <summary> 相同纬度比较运算栗子 </summary>

``` python
>>> a = pd.DataFrame(np.arange(12).reshape(3,4))
>>> a
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
 
>>> d = pd.DataFrame(np.arange(12,0,-1).reshape(3,4))
>>> d
    0   1   2  3
0  12  11  10  9
1   8   7   6  5
2   4   3   2  1
 
>>> a > d
       0      1      2      3
0  False  False  False  False
1  False  False  False   True
2   True   True   True   True
 
>>> a == d
       0      1      2      3
0  False  False  False  False
1  False  False   True  False
2  False  False  False  False
```

</details>  
  
  
<details>
  <summary> 不同纬度比较运算栗子 </summary>

``` python
>>> a = pd.DataFrame(np.arange(12).reshape(3,4))
>>> a
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
>>> c = pd.Series(np.arange(4))
>>> c
0    0
1    1
2    2
3    3
dtype: int32

>>> a > c
       0      1      2      3
0  False  False  False  False
1   True   True   True   True
2   True   True   True   True
 
>>> c > 0
0    False
1     True
2     True
3     True
dtype: bool
```

</details>  
  
  
***
## 数据的排序
对一组数据的理解  
一组数据表达一个或多个含义  
摘要: 有损地踢出数据特征的过程
* 基本统计(含排序)
* 分布/累计统计
* 数据特征 相关性、周期性等
* 数据挖掘(形成知识)

#### 对索引排序
sort_index()方法在指定的轴上根据索引进行排序 默认升序。
sort_values()方法在指定的轴上根据数据进行排序 默认升序

.sort_index(axis = 0, ascending=True)
Series.sort_values(by, axis=0, ascending=True)
DataFrame.sort_values(by, axis=0, ascending=True)
* by : axis轴上的某个索引或索引列表
* ascending : 为True时 递增排序

<details>
  <summary> 对DataFrame对象的索引排序栗子 </summary>

``` python
>>> b = pd.DataFrame(np.arange(20).reshape(4,5),index = [x for x in "cadb"])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19
 
>>> b.sort_index()
    0   1   2   3   4
a   5   6   7   8   9
b  15  16  17  18  19
c   0   1   2   3   4
d  10  11  12  13  14
 
>>> b.sort_index(ascending=False)
    0   1   2   3   4
d  10  11  12  13  14
c   0   1   2   3   4
b  15  16  17  18  19
a   5   6   7   8   9
 
>>> b.sort_index(axis=1, ascending=False)
    4   3   2   1   0
c   4   3   2   1   0
a   9   8   7   6   5
d  14  13  12  11  10
b  19  18  17  16  15
```

</details>  
  
<details>
  <summary> 对DateFrame对象的数据排序栗子 </summary>

``` python
>>> b = pd.DataFrame(np.arange(20).reshape(4,5),index = [x for x in "cadb"])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19
 
>>> c = b.sort_values(2, ascending = False)
>>> c
    0   1   2   3   4
b  15  16  17  18  19
d  10  11  12  13  14
a   5   6   7   8   9
c   0   1   2   3   4

>>> c.sort_values('a', axis = 1, ascending = False)
    4   3   2   1   0
b  19  18  17  16  15
d  14  13  12  11  10
a   9   8   7   6   5
c   4   3   2   1   0
```

</details>  
  
<details>
  <summary> NaN统一放到排序末尾 </summary>

``` python
>>> a = pd.DataFrame(np.arange(12).reshape(3,4), index = [x for x in "abc"])
>>> a
   0  1   2   3
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
 
>>> b = pd.DataFrame(np.arange(20).reshape(4,5),index = [x for x in "cadb"])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19
 
>>> c = a + b
>>> c
      0     1     2     3   4
a   5.0   7.0   9.0  11.0 NaN
b  19.0  21.0  23.0  25.0 NaN
c   8.0  10.0  12.0  14.0 NaN
d   NaN   NaN   NaN   NaN NaN
 
>>> c.sort_values(2, ascending = False)
      0     1     2     3   4
b  19.0  21.0  23.0  25.0 NaN
c   8.0  10.0  12.0  14.0 NaN
a   5.0   7.0   9.0  11.0 NaN
d   NaN   NaN   NaN   NaN NaN
 
>>> c.sort_values(2, ascending = True)
      0     1     2     3   4
a   5.0   7.0   9.0  11.0 NaN
c   8.0  10.0  12.0  14.0 NaN
b  19.0  21.0  23.0  25.0 NaN
d   NaN   NaN   NaN   NaN NaN
```

</details>  
  
***
## 数据的基本统计分析
基本的统计分析函数  

* 适用于Series和DataFrame类型

方法|说明 
:--|:--
.sum()|计算数据的总和 按0轴计算 下同
.count()|非NaN值的数量
.mean() .median() | 计算数据的算术平均值、算术中位数
.var()  .std() | 计算数据的方差、标准差
.min() .max() | 计算数据的最小值、最大值
.describe() | 针对0轴(各列)的统计汇总

* 适用于Series类型

方法|说明 
:--|:--
.argmin() .argmax()|计算数据最大值、最小值所在位置的索引位置(自动索引)
.idxmin() .idxmax()|计算数据最大值、最小值所在位置的索引(自定义索引)

<details>
  <summary> Series.describe() 栗子 </summary>

``` python
>>> a = pd.Series([9,8,7,6], index = [x for x in "abcd"])
>>> a
a    9
b    8
c    7
d    6
dtype: int64
 
>>> a.describe()
count    4.000000
mean     7.500000
std      1.290994
min      6.000000
25%      6.750000
50%      7.500000
75%      8.250000
max      9.000000
dtype: float64
 
>>> type(a.describe())
<class 'pandas.core.series.Series'>
 
>>> a.describe()['count']
4.0
 
>>> a.describe()['max']
9.0
```

</details>  
  
  
<details>
  <summary> DataFrame.describe() 栗子 </summary>

``` python
>>> b = pd.DataFrame(np.arange(20).reshape(4,5), index = [x for x in "cadb"])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19
 
>>> b.describe()
               0          1          2          3          4
count   4.000000   4.000000   4.000000   4.000000   4.000000
mean    7.500000   8.500000   9.500000  10.500000  11.500000
std     6.454972   6.454972   6.454972   6.454972   6.454972
min     0.000000   1.000000   2.000000   3.000000   4.000000
25%     3.750000   4.750000   5.750000   6.750000   7.750000
50%     7.500000   8.500000   9.500000  10.500000  11.500000
75%    11.250000  12.250000  13.250000  14.250000  15.250000
max    15.000000  16.000000  17.000000  18.000000  19.000000
 
>>> type(b.describe())
<class 'pandas.core.frame.DataFrame'>
 
 # ix已弃用 新版使用 .loc
>>> b.describe().loc['max']
0    15.0
1    16.0
2    17.0
3    18.0
4    19.0
Name: max, dtype: float64

>>> b.describe()[2]
count     4.000000
mean      9.500000
std       6.454972
min       2.000000
25%       5.750000
50%       9.500000
75%      13.250000
max      17.000000
Name: 2, dtype: float64
```

</details>  
  
  
***
## 数据的累计统计分析
#### 基本统计函数
* 适用于Series和DataFrame类型

方法|说明 
:--|:--
.cumsum()|一次给出前1、2、...、n个数的和
.cumprod()|一次给出前1、2、...、n个数的积
.cummax()|一次给出前1、2、...、n个数的最大值
.cummin()|一次给出前1、2、...、n个数的最小值

<details>
  <summary> 举个栗子 </summary>

``` python
>>> b = pd.DataFrame(np.arange(20).reshape(4,5), index = [x for x in "cadb"])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19
 
>>> b.cumsum()
    0   1   2   3   4
c   0   1   2   3   4
a   5   7   9  11  13
d  15  18  21  24  27
b  30  34  38  42  46
 
>>> b.cumprod()
   0     1     2     3     4
c  0     1     2     3     4
a  0     6    14    24    36
d  0    66   168   312   504
b  0  1056  2856  5616  9576
 
>>> b.cummin()
   0  1  2  3  4
c  0  1  2  3  4
a  0  1  2  3  4
d  0  1  2  3  4
b  0  1  2  3  4
 
>>> b.cummax()
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19
```

</details>  
  
  
#### 滚动计算函数
* 适用于Series和DataFrame类型

方法|说明 
:--|:--
.rolling(w).sum()| 依次计算相邻w个元素的和
.rolling(w).mean()| 依次计算相邻w个元素的算术平均值
.rolling(w).var()| 依次计算相邻w个元素的方差
.rolling(w).std()| 依次计算相邻w个元素的标准差
.rolling(w).min() .max()| 依次计算相邻w个元素的最小值和最大值
 
  
<details>
  <summary> 举个栗子 </summary>

``` python
>>> b = pd.DataFrame(np.arange(20).reshape(4,5), index = [x for x in "cadb"])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

>>> b.rolling(2).sum()    # 21.0 是 8+13
      0     1     2     3     4
c   NaN   NaN   NaN   NaN   NaN
a   5.0   7.0   9.0  11.0  13.0
d  15.0  17.0  19.0  21.0  23.0
b  25.0  27.0  29.0  31.0  33.0

>>> b.rolling(3).sum()    # 42 是 19 + 14 + 9
      0     1     2     3     4
c   NaN   NaN   NaN   NaN   NaN
a   NaN   NaN   NaN   NaN   NaN  # 前方加自己不满足w 3行 所以NaN
d  15.0  18.0  21.0  24.0  27.0
b  30.0  33.0  36.0  39.0  42.0
```

</details>  
  
  
***
## 数据的相关分析
#### 相关分析概念
* 两个事物 表示为 X Y , 如何判断他们之间的相关性？
    * X增大 Y也增大 两个变量正相关。
    * X增大 Y减小 两个变量负相关
    * X增大 Y无视 两个变量无相关

#### 如何度量两个事物的相关性
协方差
* 协方差 > 0 , X和Y正相关。
* 协方差 < 0 , X和Y负相关。
* 协方差 = 0 , X和Y独立无关。

Pearson相关系数
怎么写数学公式啊
r 取值范围[-1,1]
越大越强相关性 反之越小

#### 相关性分析函数

方法|说明 
:--|:--
.cov()|计算协方差矩阵
.corr()|计算相关系数矩阵, Pearson、Speraman、Kendall等系数

## 总结
一组数据的摘要
* 排序 .sort_index() .sort_values()
* 基本统计函数 .describe()
* 累计统计函数 .cum*() .rolling().\*()
* 相关性分析 .corr() .cov()
