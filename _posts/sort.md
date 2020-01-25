---
title: 常用排序算法
date: 2020-1-25 23:01:17
tags: 
- python
- c
- 算法
categories:
cover: /img/sort.jpg
---



| 排序方法 | 平均时间复杂度 | 最坏时间复杂度 | 最优时间复杂度 | 空间复杂度 | 稳定性 |
| :------- | :------------- | :------------- | :------------- | :--------- | :----- |
| 冒泡排序 | O(n²)          | O(n*n)         | O(n)           | O(1)       | 稳如狗 |
| 插入排序 | O(n²)          | O(n²)          | O(n)           | O(1)       | 稳如狗 |
| 选择排序 | O(n²)          | O(n²)          | O(n²)          | O(1)       | 不稳定 |
| 快速排序 | O(nlog2n)      | O(n²)          | O(nlog2n)      | O(nlog2n)  | 不稳定 |


*** 

#### 冒泡排序  
>冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。<br>
它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果顺序（如从大到小、首字母从从Z到A）错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成。<br>这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端（升序或降序排列），就如同碳酸饮料中二氧化碳的气泡最终会上浮到顶端一样，故名“冒泡排序”。
 
<details>
  <summary> c语言代码 </summary>

``` c
# include <stdio.h>
# define ARRAY_SIZE 23
/*
思路:
    遍历数组 如果一个数是大于下一个数 那么就互换这两个值
    使得最后的数永远是最大的
*/
 
void show(char* text, int * array, int size){
    int i = 0;
    printf("%s ", text);
    while ( i < size){
        printf("%2d ",array[i]);
        i++;
    }
    printf("\n");
}
 
int main(void){
    int array[ARRAY_SIZE] = {1, 19, 2, 7, 14, 15, 20, 18, 16, 3, 6, 21, 11, 23, 22, 17, 8, 5, 4, 12, 13, 10, 9};
    show("original",array, ARRAY_SIZE);
    int temp ;
    for(int i=0; i<ARRAY_SIZE; i++){
        for(int j=i+1; j < ARRAY_SIZE; j++){
            if (array[i] > array[j]){
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }      
        }
    }
    show("new_sort",array, ARRAY_SIZE);
    return 0;
}
```

</details>  
  
  
<details>
  <summary> python绘图代码 </summary>

``` python
from config import dcolor, desc
from plt_show import show  

def bubble_sort(ordata): 
    '''gif每一帧的生成器'''
    # rtype : yield DataFrame
    data = ordata.copy(deep=True)
    i = len(data)
    while i > 1: 
        now_number = data['number'][0]
        data['color'][0] = dcolor['now']
        for j in range(1, i):
            target = data['number'][j]
            # desc 控制排序方式 默认为升序 即判断 now_number > target 否则 条件反过来
            # 如果成立 互换两个值
            if ( now_number < target if desc else now_number > target ):
                data['number'][j], data['number'][j-1] = now_number, data['number'][j]
                data['color'][j],data['color'][j-1] = data['color'][j-1],data['color'][j]
            # 如果不成立 now_number 应该等于更大的数 color互换
            else:
                now_number = data['number'][j]
                data['color'][j],data['color'][j-1] = data['color'][j-1],data['color'][j]
            # 如果本次循环已到尽头 这个数字判定为已排序 修改颜色
            if j == i-1:
                data['color'][j] = dcolor['done']
            yield data.copy(deep=True)      
        i -= 1
    # 到这一步 已经是只剩下一个数字 不需要判断 直接修改颜色
    data['color'][0] = dcolor['done']
    yield data
 
if __name__ == "__main__":  
    show(bubble_sort, title='bubble_sort', filename='gif/bubble_sort.gif')
```

</details>  
  
<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/sort_bubble_sort.gif" alt=""> 
 
***

#### 插入排序
>插入排序（Insertion sort）是一种简单直观且稳定的排序算法。如果有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，但要求插入后此数据序列仍然有序，这个时候就要用到一种新的排序方法——插入排序法,插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。<br>插入排序的基本思想是：每步将一个待排序的记录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。

* 这里python代码为了使图片更加直观 每次循环判断直接互换了两个元素 实际上算法本身一次循环只互换一次 

<details>
  <summary> c语言代码 </summary>

``` c
# include <stdio.h>
# define ARRAY_SIZE 23
/*
思路:
    每步将一个待排序的记录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。
*/
 
void show(char* text, int * array, int size){
    int i = 0;
    printf("%s ", text);
    while ( i < size){
        printf("%2d ",array[i]);
        i++;
    }
    printf("\n");
}
 
int main(void){
    int array[ARRAY_SIZE] = {1, 19, 2, 7, 14, 15, 20, 18, 16, 3, 6, 21, 11, 23, 22, 17, 8, 5, 4, 12, 13, 10, 9};
    show("original",array, ARRAY_SIZE);
    int target; 
    for(int i=1; i<ARRAY_SIZE; i++){
        target = array[i];
        int j = i-1;
        // 当存在大于target的数 这个数往后移一位
        while (j>=0 && array[j] > target){
            array[j+1] = array[j];
            j--;
        }
        // 当while结束时 j+1 > target > j-1
        // 如果这个数 跟排序好的最后一个数相等就不用交换了
        if (j != i-1){
            array[j+1] = target;
        } 
    }
    show("new_sort",array, ARRAY_SIZE);
    return 0;
}
```

</details>  
  
  
<details>
  <summary> python绘图代码 </summary>

``` python
from config import dcolor, desc
from plt_show import show  
 
def insertion_sort(ordata): 
    '''gif每一帧的生成器'''
    # rtype : yield DataFrame
    data = ordata.copy(deep=True)
    for i in range(len(data)):
        target = i
        temp = data['number'][target]
        data['color'][i] = dcolor['now']
        yield data.copy(deep=True)
        j = i-1 
        data['color'][i] = dcolor['done']
        while (j>=0) and (data['number'][j] > temp):
            data['number'][j+1] = data['number'][j] 
            data['number'][j] = temp
            data['color'][j] = dcolor['now']
            data['color'][j+1] = dcolor['done']
            j -= 1    
            yield data.copy(deep=True)  
            data['color'][j+1] = dcolor['done']
        yield data.copy(deep=True) 
 
if __name__ == "__main__":  
    show(insertion_sort, title='insertion_sort', filename='gif/insertion_sort.gif')
```

</details>  
  
<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/sort_insertion_sort.gif" alt=""> 
 
***

#### 选择排序 

>选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理是：第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾。以此类推，直到全部待排序的数据元素的个数为零。选择排序是不稳定的排序方法。
 
<details>
  <summary> c语言代码 </summary>

``` c
# include <stdio.h>
# define ARRAY_SIZE 23
/*
思路:
    找到未排序的元素的最小值
    然后和数组中未排序的 最前面的值互换
*/
 
void show(char* text, int * array, int size){
    int i = 0;
    printf("%s ", text);
    while ( i < size){
        printf("%2d ",array[i]);
        i++;
    }
    printf("\n");
}
 
int main(void){
    int array[ARRAY_SIZE] = {1, 19, 2, 7, 14, 15, 20, 18, 16, 3, 6, 21, 11, 23, 22, 17, 8, 5, 4, 12, 13, 10, 9};
    show("original",array, ARRAY_SIZE);
    int target;
    int temp;
    for(int i=0; i<ARRAY_SIZE; i++){
        target = i;
        for(int j=i+1; j < ARRAY_SIZE; j++){
            if (array[target] > array[j]){
                target = j;
            }      
        }
        temp = array[i];
        array[i] = array[target];
        array[target] = temp;
    }
    show("new_sort",array, ARRAY_SIZE);
    return 0;
}
```

</details>  
  
  
<details>
  <summary> python绘图代码 </summary>

``` python
from config import dcolor, desc
from plt_show import show  
 
def selection_sort(ordata): 
    '''gif每一帧的生成器'''
    # rtype : yield DataFrame
    data = ordata.copy(deep=True)
    for now_index in range(len(data)):
        target = now_index
        data['color'][now_index] = dcolor['now']
        for new_target in range(now_index+1,len(data)):
            data['color'][new_target] = dcolor['target'] 
            yield data.copy(deep=True)
            if ( data['number'][target] < data['number'][new_target] if desc\
                    else data['number'][target] > data['number'][new_target] ):
                data['color'][target] = dcolor['default']
                yield data.copy(deep=True)
                target = new_target
                data['color'][target] = dcolor['now'] 
            else:
                data['color'][new_target] = dcolor['default']
            yield data.copy(deep=True)
        data['color'][now_index] = dcolor['now']
        yield data.copy(deep=True)
        data['number'][now_index], data['number'][target] = data['number'][target],data['number'][now_index]
        data['color'][target] = dcolor['default']
        data['color'][now_index] = dcolor['done']
        yield data.copy(deep=True)
 
if __name__ == "__main__":  
    show(selection_sort, title='selection_sort', filename='gif/selection_sort.gif')
    
```

</details>  
  
<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/sort_selection_sort.gif" alt=""> 

***